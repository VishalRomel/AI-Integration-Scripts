from transformers import pipeline
from datasets import load_dataset 
import soundfile as sf
import torch   

# pip install --upgrade pip
# pip install --upgrade transformers sentencepiece datasets[audio]

 

#Change device to cpu instead of cuda if you dont have an NVIDIA GPU.
synthesiser = pipeline("text-to-speech", "microsoft/speecht5_tts", device="cuda")

embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
speaker_embedding = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)
# You can replace this embedding with your own as well.

speech = synthesiser("Thomas looks like jesus. Carti is mid and only got popular because of stupid ass fans.", forward_params={"speaker_embeddings": speaker_embedding})

sf.write("thomas.wav", speech["audio"], samplerate=speech["sampling_rate"])
