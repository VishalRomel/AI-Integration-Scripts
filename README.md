## AI Integration

# Project Setup Guide

## Requirements

### Python Setup

To run the Python files, ensure you have:

- Python installed (version 3.x)
- Pip installed (to install required packages)

### Java Setup

For Java files, make sure you have:

- Java JDK installed (version 8 or later)

### OpenAI Integration

To run scripts that use OpenAI:

1. Install the necessary packages:

   ```bash
   pip install openai python-dotenv
   ```

2. **How to get an OpenAI API key:**
   - Note: OpenAI usage is not free but very affordable (around $5 should be sufficient for testing).
   - Go to this [link](https://platform.openai.com/settings/profile?tab=api-keys), log in, and generate an API key.
   - You may need to navigate through the platform to find the API key generation page.
   - Ensure you have sufficient credits by purchasing them if needed.

### Hugging Face Integration

To run scripts that use Hugging Face models, install the following packages:

```bash
pip install diffusers transformers torch
```

### Hugging Face Scripts & Models

Here are the Hugging Face models used in various scripts:

- **HF_image_gen.py** uses: [Stable Diffusion v1.5](https://huggingface.co/stable-diffusion-v1-5/stable-diffusion-v1-5)
- **HF_text_to_speech.py** uses: [Microsoft SpeechT5 TTS](https://huggingface.co/microsoft/speecht5_tts)
- **HF_summary.py** uses: [BART-Large CNN](https://huggingface.co/facebook/bart-large-cnn)

---

## Troubleshooting CUDA Issues

If you encounter an error about CUDA not being enabled, follow these steps to enable CUDA support for PyTorch.

### For NVIDIA 40, 30, and 20 Series GPUs:

Use the following command to install PyTorch with CUDA 11.8 support:

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### For NVIDIA 10 Series GPUs (e.g., GTX 1060, 1070, 1080, 1660):

These GPUs are compatible with **CUDA 10.x**. To install PyTorch with CUDA 10.2, use this command:

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu102
```

This ensures that CUDA is set up correctly and that PyTorch can use your GPU for computations.

---

Let me know if you face any issues during the installation!

---

This revision improves readability, adds some structure, and makes the instructions easier to follow.
