## Installation

For finetuning: tensorboardX. peft >= 0.11.1.

## Fine-tuning

```shell
cd finetune
sh finetune_lora_custom.sh
```

## Results

Tune vision 1024:

Zero2 offload none: OOM
Zero2 offload optimizer: 32 GB
Zero3 offload params: 37 GB

Tune vision 3072:
Zero2 offload none: OOM
Zero2 offload optimizer: 39 GB (30 GB if slice_num=5)
Zero3 offload params: 37 GB