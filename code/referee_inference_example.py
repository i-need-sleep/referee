import torch

from models.deberta_for_eval import DebertaForEval
import utils.globals as uglobals

if __name__ == '__main__':
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = DebertaForEval(uglobals.DERBERTA_MODEL_DIR, uglobals.DERBERTA_TOKENIZER_DIR, device, head_type='linear')
    model.load_state_dict(torch.load(f'{uglobals.CHECKPOINTS_DIR}/simpeval/pretrained.bin', map_location=device)['model_state_dict'], strict=False)
    model.eval()

    # Example usage
    #[[complex, simplified], ...]
    sents = [
            [
                "In late 2004, Suleman made headlines by cutting Howard Stern's radio show from four Citadel stations, citing Stern's frequent discussions regarding his upcoming move to Sirius Satellite Radio.",
                "In late 2004, suleman made headlines by cutting howard stern 's radio show from four citadel stations."
            ],
            [
                "In late 2004, Suleman made headlines by cutting Howard Stern's radio show from four Citadel stations, citing Stern's frequent discussions regarding his upcoming move to Sirius Satellite Radio.",
                "In late 2004, suleman made headlines by cutting howard stern 's radio show from four citadel stations, referring to Stern's frequent discussions regarding his upcoming move to Sirius Satellite Radio."
            ],

        ]
    
    for i, pair in enumerate(sents):
        model_input = [str(pair[0]) + ' ' + model.tokenizer.sep_token + ' ' + str(pair[1])]
        model_out = model(model_input)
        score = model_out[:, -1].item()
        print(pair)
        print(score)