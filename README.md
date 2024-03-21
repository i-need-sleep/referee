# Code and data for REFeREE: A REference-FREE Model-Based Metric for Text Simplification (LERC-COLING 2024).

## Inference
* Install the requirements:
```
pip install -r requirements.txt
```

* Download the pretrained DeBERTa tokenizer using [fetch_huggingface_models.py](https://github.com/i-need-sleep/referee/blob/main/code/utils/fetch_huggingface_models.py).
* Download the finetuned DeBERTa checkpoint from [Google Drive](https://drive.google.com/file/d/1BTUIUIrV_ANp53o80oaozs0jxhOu-0lb/view?usp=sharing) and put it under results/checkpoints/simpeval/pretained.bin.
* Modify and run [referee_inference_example.py](https://github.com/i-need-sleep/referee/blob/main/code/referee_inference_example.py).

## Training
* Generate the pretraining/finetuning data.
* Modify and run [train_debeta.py](https://github.com/i-need-sleep/referee/blob/main/code/train_deberta.py).

## Citation
