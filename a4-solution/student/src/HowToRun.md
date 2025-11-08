# Baseline London:
```bash
python src/london_baseline.py --dev_path birth_dev.tsv
```

# Vanilla model (no RoPE):

## Fine-tune (không pretrain):
```bash
python src/run.py finetune vanilla wiki.txt --writing_params_path vanilla.model.params --finetune_corpus_path birth_places_train.tsv
```

## Evaluate dev/test (no pretrain):
```bash
python src/run.py evaluate vanilla wiki.txt --reading_params_path vanilla.model.params --eval_corpus_path birth_dev.tsv --outputs_path vanilla.nopretrain.dev.predictions
python src/run.py evaluate vanilla wiki.txt --reading_params_path vanilla.model.params --eval_corpus_path birth_test_inputs.tsv --outputs_path vanilla.nopretrain.test.predictions 
```

## Pretrain (span corruption):
```bash
python src/run.py pretrain vanilla wiki.txt --writing_params_path vanilla.pretrain.params
```

## Fine-tune (load pretrained):
```bash
python src/run.py finetune vanilla wiki.txt --reading_params_path vanilla.pretrain.params --writing_params_path vanilla.finetune.params --finetune_corpus_path birth_places_train.tsv
```

## Evaluate dev/test (load pretrained):
```bash
python src/run.py evaluate vanilla wiki.txt --reading_params_path vanilla.finetune.params --eval_corpus_path birth_dev.tsv --outputs_path vanilla.pretrain.dev.predictions
python src/run.py evaluate vanilla wiki.txt --reading_params_path vanilla.finetune.params --eval_corpus_path birth_test_inputs.tsv --outputs_path vanilla.pretrain.test.predictions
```

### Note: Nếu bị lỗi như sau:
```
RuntimeError:
        An attempt has been made to start a new process before the
        current process has finished its bootstrapping phase.

        This probably means that you are not using fork to start your
        child processes and you have forgotten to use the proper idiom
        in the main module:

            if __name__ == '__main__':
                freeze_support()
                ...

        The "freeze_support()" line can be omitted if the program
        is not going to be frozen to produce an executable.
```
Thì chạy src/run_on_window_cpu.py thay vì run.py
