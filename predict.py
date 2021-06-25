from pytorch_transformer import Transformer
from data_utils import *
from util import *
import argparse


def trans(sent):
    kor, eng = get_kor_eng_sentences()
    sentences = {'src_lang': kor, 'tgt_lang': eng}
    tokens = get_tokens(sentences, 1)
    vocabs = build_vocabs(sentences, tokens)
    model = torch.load('checkpoints/script_checkpoint_mod.pt')
    text_transform = get_text_transform(tokens, vocabs)
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model.to(device)
    result = translate(model, sent.input, vocabs, text_transform, device)
    print("\noutput: {}".format(result))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Korean to English Translation')
    parser.add_argument('--input', type=str, default="나는 배고프다.", help="YOUR_INPUT")
    sent = parser.parse_args()
    trans(sent)