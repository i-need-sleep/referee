# Code and data for REFeREE: A REference-FREE Model-Based Metric for Text Simplification (LERC-COLING 2024).

## Inference
* Install the requirements:
```
pip install -r requirements.txt
```

* Download the pretrained DeBERTa tokenizer using [fetch_huggingface_models.py]().
* Download the finetuned DeBERTa checkpoint from [Google Drive]() and put it under results/checkpoints/simpeval/pretained.bin.
* Modify and run [referee_inference_example.py]().

## Training
* Generate the pretraining/finetuning data. Or download them from [Google Drive]().
* Modify and run [train_debeta.py]().

## Citation