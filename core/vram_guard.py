"""
⚡ Proactive GPU VRAM Guard & Memory Allocator
Prevents CUDA Out-Of-Memory (OOM) errors on Google Colab (15GB T4)
and optimizes Dual T4 tensor parallelism on Kaggle.
"""

import os
import gc
from typing import Dict, Any, List

def optimize_gpu_memory(max_memory_fraction: float = 0.90) -> Dict[str, Any]:
    """
    Configures PyTorch memory allocator to eliminate fragmentation deadlocks
    and enforces safe allocation fractions.
    """
    # 1. Expandable segments eliminate PyTorch memory fragmentation spikes
    os.environ.setdefault("PYTORCH_CUDA_ALLOC_CONF", "expandable_segments:True")
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    os.environ["OLLAMA_NUM_PARALLEL"] = "1"
    os.environ["OLLAMA_KEEP_ALIVE"] = "24h"

    # Avoid Flax / TensorFlow deprecation noise and slow memory hogging in Colab
    os.environ["USE_FLAX"] = "0"
    os.environ["USE_TF"] = "0"

    gpu_info: List[Dict[str, Any]] = []

    try:
        import torch
        if torch.cuda.is_available():
            device_count = torch.cuda.device_count()
            for i in range(device_count):
                total_bytes = torch.cuda.get_device_properties(i).total_memory
                total_gb = round(total_bytes / (1024 ** 3), 2)
                name = torch.cuda.get_device_name(i)

                try:
                    torch.cuda.set_per_process_memory_fraction(max_memory_fraction, i)
                except Exception:
                    pass

                gpu_info.append({
                    "device_index": i,
                    "name": name,
                    "total_vram_gb": total_gb,
                    "usable_vram_gb": round(total_gb * max_memory_fraction, 2)
                })

            torch.cuda.empty_cache()
            gc.collect()

            return {
                "status": "success",
                "cuda_available": True,
                "device_count": device_count,
                "devices": gpu_info
            }
    except Exception as e:
        return {
            "status": "warning",
            "cuda_available": False,
            "error": str(e),
            "devices": []
        }

    return {
        "status": "cpu_only",
        "cuda_available": False,
        "devices": []
    }

def clear_vram_cache() -> None:
    """
    Forces immediate garbage collection and releases cached VRAM back to the GPU driver.
    """
    gc.collect()
    try:
        import torch
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
            torch.cuda.ipc_collect()
    except Exception:
        pass
