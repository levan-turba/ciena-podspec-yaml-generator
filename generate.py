from pathlib import Path

base_yaml_str = open("base_yaml.yaml").read()
node_gpu_uuids = {"SERVER_A": "GPU-AAAAAAAA-AAAA-AAAA-AAAA-AAAAAAAAAAAA",
                  "SERVER_B": "GPU-BBBBBBBB-BBBB-BBBB-BBBB-BBBBBBBBBBBB",
                  "SERVER_C": "GPU-CCCCCCCC-CCCC-CCCC-CCCC-CCCCCCCCCCCC",
                  "SERVER_D": "GPU-DDDDDDDD-DDDD-DDDD-DDDD-DDDDDDDDDDDD"}


baseline_models = {
    "deepseek-r1-7b": {
        "hf_name": "lmstudio-community/DeepSeek-R1-Distill-Qwen-7B-GGUF/resolve/main/DeepSeek-R1-Distill-Qwen-7B-Q8_0.gguf",
        "node_name": "SERVER_A",
        "mig_profile": "7g.40gb",
        "mig_index": 0,
    },
    "llama-3.3-70b-instruct-1": {
        "hf_name": "lmstudio-community/Llama-3.3-70B-Instruct-GGUF/resolve/main/Llama-3.3-70B-Instruct-Q3_K_M.gguf",
        "node_name": "SERVER_B",
        "mig_profile": "7g.40gb",
        "mig_index": 0,
    },
    "llama-3.2-1b-instruct-1": {
        "hf_name": "lmstudio-community/Llama-3.2-1B-Instruct-GGUF/resolve/main/Llama-3.2-1B-Instruct-Q8_0.gguf",
        "node_name": "SERVER_C",
        "mig_profile": "7g.40gb",
        "mig_index": 0,
    },
    "llama-3.3-70b-instruct-2": {
        "hf_name": "lmstudio-community/Llama-3.3-70B-Instruct-GGUF/resolve/main/Llama-3.3-70B-Instruct-Q3_K_M.gguf",
        "node_name": "SERVER_D",
        "mig_profile": "7g.40gb",
        "mig_index": 0,
    },
}

turba1_models = {
    # SERVER_A
    # 4g.20gb at slice 0 saved for swapper
    "llama-3.2-1b-instruct-1": {
        "hf_name": "lmstudio-community/Llama-3.2-1B-Instruct-GGUF/resolve/main/Llama-3.2-1B-Instruct-Q8_0.gguf",
        "node_name": "SERVER_A",
        "mig_profile": "1g.5gb",
        "mig_index": 4,
    },
    "llama-3.2-1b-instruct-2": {
        "hf_name": "lmstudio-community/Llama-3.2-1B-Instruct-GGUF/resolve/main/Llama-3.2-1B-Instruct-Q8_0.gguf",
        "node_name": "SERVER_A",
        "mig_profile": "1g.5gb",
        "mig_index": 5,
    },
    "deepseek-r1-1.5b-1": {
        "hf_name": "lmstudio-community/DeepSeek-R1-Distill-Qwen-1.5B-GGUF/resolve/main/DeepSeek-R1-Distill-Qwen-1.5B-Q8_0.gguf",
        "node_name": "SERVER_A",
        "mig_profile": "1g.10gb",
        "mig_index": 6,
    },

    # SERVER_B
    "llama-3.3-70b-instruct-1": {
        "hf_name": "lmstudio-community/Llama-3.3-70B-Instruct-GGUF/resolve/main/Llama-3.3-70B-Instruct-Q3_K_M.gguf",
        "node_name": "SERVER_B",
        "mig_profile": "7g.40gb",
        "mig_index": 0,
    },

    # SERVER_C
    "deepseek-r1-7b-1": {
        "hf_name": "lmstudio-community/DeepSeek-R1-Distill-Qwen-7B-GGUF/resolve/main/DeepSeek-R1-Distill-Qwen-7B-Q8_0.gguf",
        "node_name": "SERVER_C",
        "mig_profile": "4g.20gbgb",
        "mig_index": 0,
    },
    "minicpm-v2.5-1": {
        "hf_name": "openbmb/MiniCPM-V-2_6-int4",
        "node_name": "SERVER_C",
        "mig_profile": "2g.10gb",
        "mig_index": 4,
    },
    "qwen2-1.5b-1": {
        "hf_name": "Qwen/Qwen2-1.5B",
        "node_name": "SERVER_C",
        "mig_profile": "1g.10gb",
        "mig_index": 6,
    },

    # SERVER_D
    "llama-3.3-70b-instruct-2": {
        "hf_name": "lmstudio-community/Llama-3.3-70B-Instruct-GGUF/resolve/main/Llama-3.3-70B-Instruct-Q3_K_M.gguf",
        "node_name": "SERVER_D",
        "mig_profile": "7g.40gb",
        "mig_index": 0,
    },
}

turba2_models = {
    # SERVER_A
    # 4g.20gb at slice 0 saved for swapper
    "llama-3.2-1b-instruct-1": {
        "hf_name": "lmstudio-community/Llama-3.2-1B-Instruct-GGUF/resolve/main/Llama-3.2-1B-Instruct-Q8_0.gguf",
        "node_name": "SERVER_A",
        "mig_profile": "1g.5gb",
        "mig_index": 4,
    },
    "llama-3.2-1b-instruct-2": {
        "hf_name": "lmstudio-community/Llama-3.2-1B-Instruct-GGUF/resolve/main/Llama-3.2-1B-Instruct-Q8_0.gguf",
        "node_name": "SERVER_A",
        "mig_profile": "1g.5gb",
        "mig_index": 5,
    },
    "deepseek-r1-1.5b-1": {
        "hf_name": "lmstudio-community/DeepSeek-R1-Distill-Qwen-1.5B-GGUF/resolve/main/DeepSeek-R1-Distill-Qwen-1.5B-Q8_0.gguf",
        "node_name": "SERVER_A",
        "mig_profile": "1g.10gb",
        "mig_index": 6,
    },

    # SERVER_B
    "llama-3.3-70b-instruct-1": {
        "hf_name": "lmstudio-community/Llama-3.3-70B-Instruct-GGUF/resolve/main/Llama-3.3-70B-Instruct-Q3_K_M.gguf",
        "node_name": "SERVER_B",
        "mig_profile": "7g.40gb",
        "mig_index": 0,
    },

    # SERVER_C
    "llama-3.3-70b-instruct-2": {
        "hf_name": "lmstudio-community/Llama-3.3-70B-Instruct-GGUF/resolve/main/Llama-3.3-70B-Instruct-Q3_K_M.gguf",
        "node_name": "SERVER_C",
        "mig_profile": "7g.40gb",
        "mig_index": 0,
    },

    # SERVER_D
    "deepseek-r1-7b-1": {
        "hf_name": "lmstudio-community/DeepSeek-R1-Distill-Qwen-7B-GGUF/resolve/main/DeepSeek-R1-Distill-Qwen-7B-Q8_0.gguf",
        "node_name": "SERVER_D",
        "mig_profile": "4g.20gbgb",
        "mig_index": 0,
    },
    "minicpm-v2.5-1": {
        "hf_name": "openbmb/MiniCPM-V-2_6-int4",
        "node_name": "SERVER_D",
        "mig_profile": "2g.10gb",
        "mig_index": 4,
    },
    "qwen2-1.5b-1": {
        "hf_name": "Qwen/Qwen2-1.5B",
        "node_name": "SERVER_D",
        "mig_profile": "1g.10gb",
        "mig_index": 6,
    },
}

for model_dir, models in (("baseline", baseline_models), ("turba1", turba1_models), ("turba2", turba2_models)):
    directory_path = Path(model_dir)
    directory_path.mkdir(exist_ok=True)
    for name, model in models.items():
        gpu_uuid = node_gpu_uuids[model["node_name"]]
        current_model_yaml = (base_yaml_str.replace("MODELNAMEHERE", name)
                              .replace("MODELHFNAMEHERE", model["hf_name"])
                              .replace("NODENAMEHERE", model["node_name"])
                              .replace("GPUUUIDHERE", gpu_uuid)
                              .replace("MIGPROFILEHERE", model["mig_profile"])
                              .replace("MIGINDEXHERE", str(model["mig_index"])))
        directory_path.joinpath(f"{name}.yaml").write_text(current_model_yaml)
