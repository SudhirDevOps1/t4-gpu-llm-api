# 🚀 Personal AI Notebook Store & Multi-Cloud GPU Hub

Welcome to your **Personal AI Notebook Store & Hub** — a production-grade, privacy-first collection of cloud GPU notebooks and standalone web clients engineered for **Google Colab Free (Tesla T4 15GB)** and **Kaggle (Dual Tesla T4 x2 30GB)**.

[![Store Web App](https://img.shields.io/badge/Obsidian_Store_Web_App-Live_Catalog-10b981?style=for-the-badge&logo=googlechrome&logoColor=white)](https://sudhirdevops1.github.io/t4-gpu-llm-api/)
[![Zero-Leak Privacy](https://img.shields.io/badge/Security-100%25_Zero--Leak-06b6d4?style=for-the-badge&logo=shield&logoColor=white)](#-zero-leak-privacy--security-architecture)
[![Google Colab](https://img.shields.io/badge/Google_Colab-Free_T4_GPU-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white)](#-notebook-catalog)
[![Kaggle](https://img.shields.io/badge/Kaggle-Dual_T4_x2-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)](#-notebook-catalog)
[![Lightning AI](https://img.shields.io/badge/Lightning_AI-Open_Studio-792EE5?style=for-the-badge&logo=lightning&logoColor=white)](https://lightning.ai/new?repo_url=https://github.com/SudhirDevOps1/t4-gpu-llm-api)
[![Chat Client](https://img.shields.io/badge/Chat_Client-Next--Gen_Workspace-8b5cf6?style=for-the-badge&logo=webrtc&logoColor=white)](https://sudhirdevops1.github.io/t4-gpu-llm-api/colab_ai_chat.html)

---

## 🎨 Interactive Obsidian Storefront

Explore, search, filter, and inspect detailed specs for all notebooks in our standalone **In-App Web Store**:

👉 [**Open AI Notebook Store Web App (`store/index.html`)**](store/index.html)

- 🔍 **Instant Search & Tag Filtering:** Quickly filter across LLMs, Audio/TTS, Vision, and Video models.
- 💻 **Platform Toggles:** One-click filter between **Google Colab (Free T4)** and **Kaggle (Dual T4 x2)**.
- 📊 **Live Spec Sheets:** Check exact VRAM footprints, memory quantization, and runtime timeout limits.
- 🛡️ **Zero Native Popups:** 100% custom in-app glassmorphism dialogs and toast notifications.

---

## 📚 Notebook Catalog

| Notebook & Model | Platform | VRAM Budget | 1-Click Launch | Capabilities & Specs |
| :--- | :--- | :--- | :--- | :--- |
| **01. T4 GPU LLM Server & OpenAI API Hub**<br>`Qwen2.5-Coder 7B` · `DeepSeek-R1 8B` | **Google Colab**<br>`Tesla T4 (15.3 GB)` | **~4.5 GB**<br>*(10GB free for KV-cache)* | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SudhirDevOps1/t4-gpu-llm-api/blob/main/t4-gpu-llm-api.ipynb) | High-speed OpenAI `/v1` server, CORS enabled, Cloudflare Tunnel without pipe deadlocks, token streaming HUD, and next-gen chat client. |
| **02. Zero-Shot Voice Cloning & TTS Studio**<br>`Kokoro TTS` · `Fish Audio S2.1` | **Google Colab**<br>`Tesla T4 / CPU` | **~2.8 GB**<br>*(CPU-friendly)* | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SudhirDevOps1/t4-gpu-llm-api/blob/main/colab/02_zero_shot_voice_tts.ipynb) | 80+ languages, crystal clear 24kHz/48kHz audio, zero-shot voice design, paralinguistic emotions, and zero HF token leaks. |
| **03. Qwen-Image 2.1 Fast INT8 Studio**<br>`Qwen-Image 2.1` · `SDXL Turbo` | **Google Colab**<br>`Tesla T4 (15.3 GB)` | **~8.2 GB**<br>*(INT8 Tensor Cores)* | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SudhirDevOps1/t4-gpu-llm-api/blob/main/colab/03_qwen_image_gen_studio.ipynb) | High-speed 1-2 step diffusion, text-to-image, instruction editing, multi-reference composition, offloaded checkpoint caching. |
| **04. Wan2.1 & LTX-Video DiT Studio**<br>`Wan2.1-1.3B` · `LTX-Video 0.9.1` | **Google Colab**<br>`Tesla T4 (15.3 GB)` | **~8.5 GB**<br>*(FP8 / INT8)* | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SudhirDevOps1/t4-gpu-llm-api/blob/main/colab/04_wan_ltx_video_studio.ipynb) | Fast diffusion transformer video generation (text-to-video & image-to-video) with procedural smooth stream rendering on Free T4. |
| **05. ComfyUI Portable Cloud Studio**<br>`ComfyUI Core` · `ComfyUI-Manager` | **Google Colab**<br>`Tesla T4 (15.3 GB)` | **~4.0 - 14.0 GB**<br>*(FP16-VAE)* | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SudhirDevOps1/t4-gpu-llm-api/blob/main/colab/05_comfyui_cloud_studio.ipynb) | 1-click cloud ComfyUI workspace with pre-installed ComfyUI-Manager and Cloudflare Tunnel to port 8188. No local ports required. |
| **06. RAG Knowledge Agent & Vector QA**<br>`all-MiniLM-L6-v2` · `ChromaDB` | **Google Colab**<br>`Tesla T4 / CPU` | **~1.2 GB**<br>*(Lightweight)* | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SudhirDevOps1/t4-gpu-llm-api/blob/main/colab/06_rag_knowledge_agent.ipynb) | Multi-format document ingestion (PDF, Markdown, Code) with cosine vector retrieval connected directly to our Colab `/v1` server. |
| **08. F5-TTS & Chatterbox Hindi Voice Clone**<br>F5-TTS · Chatterbox-Turbo | **Google Colab**<br>Tesla T4 (15.3 GB) | **~3.5 GB**<br>*(Ultra-Fast)* | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SudhirDevOps1/t4-gpu-llm-api/blob/main/colab/08_f5_chatterbox_hindi_voice.ipynb) | ElevenLabs open-source alternative. Zero-shot cloning (3-10s clip), native Hindi & Hinglish support, and Chatterbox emotion exaggeration slider. |
| **07. QLoRA 4-bit Fine-Tuning Studio**<br>`BitsAndBytes NF4` · `PEFT / TRL` | **Google Colab**<br>`Tesla T4 (15.3 GB)` | **~9.5 GB**<br>*(4-bit NF4)* | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SudhirDevOps1/t4-gpu-llm-api/blob/main/colab/07_qlora_training_studio.ipynb) | Fine-tune 7B/8B parameter LLMs on a single free 15GB T4 GPU with gradient checkpointing and safe `.safetensors` adapter export. |
| **10. Kaggle Dual T4 x2 Distributed LLM Engine**<br>`DeepSeek-R1 14B` · `Qwen2.5 14B` | **Kaggle**<br>`Dual T4 x2 (30.6 GB)` | **~14.0 GB**<br>*(Tensor Parallel)* | [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://www.kaggle.com/code/new) | Distributed multi-GPU inference on Kaggle Dual Tesla T4 x2, 30h/week free quota, isolated instance tokens, and `/v1` endpoint. |
| **10. Kaggle Dual T4 x2 ComfyUI Studio**<br>`ComfyUI` · `Dual T4 Tensor Parallel` | **Kaggle**<br>`Dual T4 x2 (30.6 GB)` | **~12.0 GB**<br>*(Dual GPU)* | [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://www.kaggle.com/code/new) | Heavy diffusion and video node workflows on Kaggle Dual Tesla T4 x2 with 30GB combined VRAM and persistent Cloudflare tunnel. |

---

---

## 🌟 Master AI Models Guide (Best for Colab Free T4 & Kaggle Dual T4)

A research-backed breakdown of the top open-source models optimized for free cloud GPUs:

### 🎙️ 1. ElevenLabs Open-Source Alternatives (Hindi, Voice Cloning & Emotions)
| Model | Developer / Architecture | VRAM | Key Features & Hindi Support |
| :--- | :--- | :--- | :--- |
| **F5-TTS / IndicF5** | Flow-Matching Architecture | ~3.5 GB | **Best Zero-Shot Voice Clone:** Clones any voice from a 3–5 sec audio sample. Superb native **Hindi** and **Hinglish** code-mixing with natural cadence and breath sounds. |
| **Resemble Chatterbox** | Resemble AI · Llama Backbone | ~3.0 GB | **Emotion Controls:** World's first open-source model with emotion exaggeration sliders and paralinguistic tags ([laugh], [sigh], [whisper], [chuckle]). |
| **VoxCPM2** | OpenBMB · Tokenizer-free | ~4.2 GB | **Studio Quality (48kHz):** Broadcast-grade speech across 30+ languages including native Hindi with voice design controls. |
| **VibeVoice-Hindi** | Qwen Backbone + Diffusion Head | ~5.0 GB | **Long-Form Audio:** Perfect for multi-speaker podcasts, audiobooks, and expressive dialogues in Hindi. |

---

### 🔓 2. Uncensored & Refusal-Free AI Models (Abliteration)
Unlike base corporate models that refuse legitimate coding, pentesting, or creative prompts, **Abliterated Models** use mathematical null-space projection to selectively remove refusal vectors without harming intelligence:
- **Qwen-2.5-Coder-7B-Abliterated:** Follows complex low-level code, reverse engineering, exploit analysis, and scripts without preachy refusals.
- **Dolphin-2.9.2-Llama-3-8B:** Generalist conversational and reasoning model with zero guardrail refusals.
- **Qwen-Image-2.1-Uncensored (INT8):** Uncensored visual diffusion model running on Tesla T4 Tensor Cores.

---

### 💻 3. Coding, Reasoning & Multi-Modal SOTA Stack
- **Deep Reasoning (CoT):** DeepSeek-R1 (7B, 8B, 14B) & Phi-4 14B for mathematical derivations and algorithm design.
- **SOTA Coding:** Qwen2.5-Coder 7B / 14B — competitive with GPT-4o on HumanEval and SWE-bench.
- **Vision & Image Generation:** Flux.1 Schnell INT8, SDXL Turbo, and Qwen-Image 2.1.
- **High-Speed Video:** Wan2.1-T2V-1.3B & LTX-Video 2.5 (720p 24fps in 8–16 steps).
- **Music & Audio:** YuE 2-3B (full-song 48kHz music generation) and ACE-Step 1.5 (LoRA music studio).

## 🛡️ Zero-Leak Privacy & Security Architecture

Unlike public community notebooks that encourage typing plaintext API keys or HuggingFace tokens into cell inputs, this store enforces an **enterprise zero-leak policy** via [`core/security.py`](core/security.py):

```mermaid
flowchart TD
    Run([🚀 Notebook Run]) --> PlatformCheck{Detect Cloud Platform}
    PlatformCheck -->|Google Colab| ColabUserData[🔒 google.colab.userdata]
    PlatformCheck -->|Kaggle| KaggleSecrets[🔒 kaggle_secrets.UserSecretsClient]
    PlatformCheck -->|Local / CLI| EnvVar[🔑 OS Environment Variables]
    
    ColabUserData --> SecretFound{Secret Found?}
    KaggleSecrets --> SecretFound
    EnvVar --> SecretFound
    
    SecretFound -->|Yes| SecureMemory[⚡ Injected in Memory Only]
    SecretFound -->|No / Fallback| MaskedPrompt[🔐 Interactive getpass - No Console Echo]
    
    MaskedPrompt --> SecureMemory
    SecureMemory --> ModelDownload[📥 Download Ungated Weights - Zero Git Commit Leak]
```

1. **Encrypted Secret Handlers:** Automatically queries Colab `userdata` or Kaggle `UserSecretsClient`. 
2. **Zero Console Echo:** Fallbacks use `getpass.getpass()`, preventing tokens from appearing in browser DOM, cell outputs, or saved `.ipynb` files.
3. **Pre-Commit Sanitization:** Notebook outputs are cleared before commits (`execution_count: null`, `outputs: []`), and `.gitignore` blocks all credential patterns (`*.key`, `*.token`, `*.pem`, `*.env`).

---

## 🆔 Unique Session Fingerprints & Limitation IDs

To prevent cross-session tunnel collisions and isolate resource quotas, every notebook run generates a dynamic fingerprint via [`core/instance.py`](core/instance.py):

```python
# Generated automatically on Cell 1 execution
INSTANCE_ID = "colab-llm-a8f3b92c"   # Unique to your runtime session
TUNNEL_TOKEN = "token-71e428a9b31d"   # Ephemeral access token
```

### Resource Quota & Hardware Budgeting:
- **Google Colab Free:** 12-hour maximum execution timeout · 60-minute idle disconnect · Single Tesla T4 (15.3 GB VRAM).
- **Kaggle Free:** 9-hour maximum execution timeout · 30 hours/week GPU quota · Dual Tesla T4 x2 (30.6 GB Total VRAM).
- **VRAM Guard (`core/vram_guard.py`):** Automatically enables PyTorch `expandable_segments:True` and forces memory fraction limits to eliminate CUDA OOM errors.

---

## 💻 Standalone Chat Client (`colab_ai_chat.html`)

Our dedicated Obsidian-themed single-page web app provides an IDE-grade chat environment for your Colab/Kaggle LLM endpoint:

- 🔮 **Glowing 3D AI Orb:** Real-time visual feedback and quick-connect modal.
- 💻 **Mac-Style Code Windows:** Syntax highlighting, 1-click **Copy**, 1-click **Download as File**, and **Live HTML Sandbox Preview**.
- 🧠 **DeepSeek-R1 Native CoT:** Beautiful accordion view for Chain-of-Thought reasoning.
- ⚡ **Realtime Token HUD:** Live tokens/second, time-to-first-token (TTFT), and token count metrics.
- 🎙️ **Voice Dictation:** Hands-free speech-to-text via Web Speech API.
- 🛡️ **Zero Native Popups:** 100% custom in-app modals and glassmorphic toast notifications.

---

## 🚀 Quick Start Guide

### 1. Launch on Google Colab:
1. Click any **Open in Colab** badge in the catalog table above.
2. Select hardware: **Runtime &rarr; Change runtime type &rarr; T4 GPU**.
3. Run **Step 1 to Step 5**. Copy the generated `https://xxxx.trycloudflare.com/v1` URL.
4. Run **Step 6** to download `colab_ai_chat.html`, paste your URL, and enjoy lag-free inference!

### 2. Launch on Kaggle:
1. Click the **Open in Kaggle** badge to create a new notebook.
2. Under **Settings**:
   - Set **Accelerator** to **GPU T4 x2**.
   - Set **Internet** to **On**.
3. Import `kaggle/01_dual_t4_llm_engine.ipynb` and run all cells sequentially.

---

## 📂 Repository Directory Structure

```
.
├── README.md                              # 🌟 Storefront catalog, badges & architecture
├── colab_ai_chat.html                     # 🎨 Next-gen obsidian client for Colab/Kaggle APIs
├── store/
│   └── index.html                         # 🛍️ Interactive Obsidian Notebook Store Catalog
├── core/
│   ├── __init__.py                        # 📦 Core package init
│   ├── security.py                        # 🛡️ Zero-leak secret loader (Colab + Kaggle)
│   ├── instance.py                        # 🆔 Dynamic session fingerprint & limitation IDs
│   └── vram_guard.py                      # ⚡ Proactive VRAM budget allocator & OOM guard
├── colab/
│   ├── 01_t4_gpu_llm_api.ipynb            # ⚡ Colab T4 LLM Server & OpenAI API Hub
│   ├── 02_zero_shot_voice_tts.ipynb       # 🎙️ Zero-Shot Voice Cloning & TTS Studio
│   ├── 03_qwen_image_gen_studio.ipynb     # 🎨 Qwen-Image 2.1 Fast INT8 Studio
│   ├── 04_wan_ltx_video_studio.ipynb      # 🎬 Wan2.1 & LTX-Video DiT Studio
│   ├── 05_comfyui_cloud_studio.ipynb      # 🎨 ComfyUI Portable Cloud Studio
│   ├── 06_rag_knowledge_agent.ipynb       # 🧠 RAG Knowledge Agent & Vector QA
│   ├── 07_qlora_training_studio.ipynb     # ⚡ QLoRA 4-bit Model Fine-Tuning Studio
│   └── 08_f5_chatterbox_hindi_voice.ipynb # 🎙️ F5-TTS & Chatterbox Hindi Voice Clone
├── kaggle/
│   ├── 01_dual_t4_llm_engine.ipynb        # 🔥 Kaggle Dual T4 x2 Distributed LLM Engine
│   └── 02_comfyui_dual_t4.ipynb           # 🎨 Kaggle Dual T4 ComfyUI & DiT Studio
└── .gitignore                             # 🔒 Strict protection against token/secret leaks
```

---

## 🤝 Contributing & Maintenance

Notebooks in this repository are actively tested and verified. If you run into any dependency shifts or upstream weight changes:
1. Open an issue on this repository.
2. Include your **Notebook Name**, **Platform (Colab/Kaggle)**, and complete error traceback.

*Crafted with passion for AI developers and open-source practitioners.*
