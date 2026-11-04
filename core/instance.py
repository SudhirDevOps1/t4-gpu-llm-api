"""
🆔 Dynamic Session Fingerprint & Instance Limitation Manager
Provides isolated instance IDs for Colab and Kaggle sessions, preventing
tunnel endpoint collisions and managing runtime quotas.
"""

import os
import time
import uuid
import socket
import hashlib
from typing import Dict, Any

def detect_platform() -> str:
    """
    Identifies whether the current runner is Google Colab, Kaggle, or Local.
    """
    if "COLAB_GPU" in os.environ or os.path.exists("/content"):
        return "colab"
    if "KAGGLE_KERNEL_RUN_TYPE" in os.environ or os.path.exists("/kaggle"):
        return "kaggle"
    return "local"

def get_platform_limits() -> Dict[str, Any]:
    """
    Returns runtime limits and timeout budgets for the detected platform.
    """
    platform = detect_platform()
    if platform == "colab":
        return {
            "platform": "Google Colab",
            "tier": "Free / Pro",
            "max_runtime_hours": 12.0,
            "max_idle_minutes": 60,
            "typical_gpu": "NVIDIA Tesla T4 (15.3 GB VRAM)",
            "system_ram_gb": 12.7,
            "root_path": "/content"
        }
    elif platform == "kaggle":
        return {
            "platform": "Kaggle",
            "tier": "Free (30h/week)",
            "max_runtime_hours": 9.0,
            "max_idle_minutes": 40,
            "typical_gpu": "Dual NVIDIA Tesla T4 x2 (30.6 GB Total VRAM)",
            "system_ram_gb": 29.0,
            "root_path": "/kaggle/working"
        }
    return {
        "platform": "Local Workstation",
        "tier": "Self-Hosted",
        "max_runtime_hours": float("inf"),
        "max_idle_minutes": float("inf"),
        "typical_gpu": "Custom GPU",
        "system_ram_gb": "Custom",
        "root_path": os.getcwd()
    }

def generate_session_instance(prefix: str = "agy") -> Dict[str, Any]:
    """
    Generates a unique session fingerprint for this run to avoid cross-session
    tunnel conflicts and enable discrete limitation IDs.
    """
    platform_name = detect_platform()
    timestamp = time.time()
    raw_fingerprint = f"{platform_name}-{socket.gethostname()}-{uuid.uuid4()}-{timestamp}"
    instance_hash = hashlib.sha256(raw_fingerprint.encode()).hexdigest()[:8]
    instance_id = f"{prefix}-{platform_name}-{instance_hash}"

    return {
        "instance_id": instance_id,
        "platform": platform_name,
        "created_at": timestamp,
        "tunnel_token": hashlib.md5(f"token-{instance_hash}".encode()).hexdigest()[:16],
        "limits": get_platform_limits()
    }
