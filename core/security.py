"""
🛡️ Zero-Leak Secret & Privacy Manager
Guarantees that API keys, HuggingFace tokens, and private credentials
are never hardcoded or printed to stdout in Google Colab, Kaggle, or Local environments.
"""

import os
import sys
import getpass
from typing import Optional

def get_secret(key_name: str, prompt_text: Optional[str] = None, default: str = "") -> str:
    """
    Safely retrieves a private credential without exposing it in notebook outputs.
    
    Priority Order:
    1. Google Colab UserData Secrets (Encrypted at rest)
    2. Kaggle UserSecretsClient (Encrypted at rest)
    3. OS Environment Variable
    4. Interactive Masked Input via getpass (Zero echo in browser or logs)
    """
    key_clean = key_name.strip()

    # 1. Google Colab UserData Secrets
    try:
        from google.colab import userdata
        val = userdata.get(key_clean)
        if val:
            return str(val).strip()
    except Exception:
        pass

    # 2. Kaggle Secrets
    try:
        from kaggle_secrets import UserSecretsClient
        val = UserSecretsClient().get_secret(key_clean)
        if val:
            return str(val).strip()
    except Exception:
        pass

    # 3. Environment Variable
    env_val = os.getenv(key_clean)
    if env_val:
        return env_val.strip()

    # 4. Interactive Masked Prompt (getpass prevents browser DOM or stdout leakage)
    try:
        prompt = prompt_text or f"🔐 Enter {key_clean} (masked, will not be shown): "
        entered = getpass.getpass(prompt)
        if entered:
            return entered.strip()
    except Exception:
        pass

    return default

def sanitize_notebook_env() -> None:
    """
    Disables telemetry, telemetry tracking, and unsafe cache buffers that can leak
    user metadata or crash low-RAM environments.
    """
    os.environ["HF_HUB_DISABLE_TELEMETRY"] = "1"
    os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "0"
    os.environ["WANDB_DISABLED"] = "true"
    os.environ["ANONYMOUS_TELEMETRY"] = "0"
