import sys; sys.path.insert(0,'work/I2/agent')
from put import put
W='https://en.wikipedia.org/wiki/'
def A(n,mk,y,s,d,v=(),a='',dt=''):
    x={"n":n,"a":a,"d":d,"mk":mk,"y":y,"s":s if s.startswith('http') else W+s,"v":[dict(n=i[0],mk=i[1],y=i[2],d=i[3]) for i in v]}
    if dt: x["dt"]=dt
    return x
kinds=[
{"n":"Language model weights","a":"AI model weights · LLM file","d":"The downloadable weights of a language model, run locally.","t":["safetensors","GGUF","Quantised (4-bit, 8-bit)","Base","Instruction-tuned"],"s":"https://huggingface.co/mistralai/Mistral-7B-v0.1/tree/main","x":[
 A("Llama","Meta AI","2023","LLaMA","Meta's model family; weights first limited to researchers, later released under use restrictions.",[
  ("Llama 1","Meta AI","2023","24 Feb 2023, 6.7B to 65.2B, non-commercial"),
  ("Llama 2","Meta AI","2023","18 Jul 2023, 7B, 13B, 70B"),
  ("Llama 3","Meta AI","2024","18 Apr 2024, 8B and 70B"),
  ("Llama 3.1","Meta AI","2024","23 Jul 2024, up to 405B"),
  ("Llama 4","Meta AI","2025","5 Apr 2025, Scout and Maverick")],"","sizes · base and instruct weights · licence terms"),
 A("Mistral 7B","Mistral AI","2023","Mistral_AI","7.3B-parameter model released by torrent and Hugging Face under Apache 2.0.",[
  ("Mistral 7B v0.1","Mistral AI","2023","27 Sep 2023, Apache 2.0"),
  ("Mixtral 8x7B","Mistral AI","2023","December 2023, Apache 2.0"),
  ("Mixtral 8x22B","Mistral AI","2024","April 2024, Apache 2.0"),
  ("Mistral Small 3","Mistral AI","2025","January 2025, 24B, Apache 2.0")]),
 A("Gemma","Google DeepMind","2024","Gemma_(language_model)","Google's open-weight family, sold on size tiers.",[
  ("Gemma 1","Google DeepMind","2024","21 Feb 2024, 2B and 7B"),
  ("Gemma 2","Google DeepMind","2024","27 Jun 2024, 2B, 9B, 27B"),
  ("Gemma 3","Google DeepMind","2025","12 Mar 2025, 1B to 27B"),
  ("Gemma 4","Google DeepMind","2026","2 Apr 2026, Apache 2.0")]),
 A("Qwen","Alibaba Cloud","2023","Qwen","Alibaba Cloud's mostly open-weight family, first released as Tongyi Qianwen beta.",[
  ("Qwen2","Alibaba Cloud","2024","June 2024"),
  ("Qwen2.5","Alibaba Cloud","2024","September 2024"),
  ("Qwen3","Alibaba Cloud","2025","28 Apr 2025, Apache 2.0")]),
 A("DeepSeek","DeepSeek","2024","DeepSeek_(AI)","Chinese open-weight family, released under the MIT licence.",[
  ("DeepSeek-V2","DeepSeek","2024","May 2024"),
  ("DeepSeek-R1","DeepSeek","2025","20 Jan 2025, MIT licence"),
  ("DeepSeek-V3","DeepSeek","2025","V3-0324 on 24 Mar 2025, MIT licence")])]},
{"n":"Image-generation model","a":"diffusion checkpoint","d":"The downloadable weights of a model that makes images from text prompts.","t":["Checkpoint","safetensors","Distilled","Base model"],"s":W+"Stability_AI","x":[
 A("Stable Diffusion","Stability AI","2022","Stability_AI","Text-to-image model released in August 2022 with source and weights available."),
 A("Flux","Black Forest Labs","2024","Flux_(text-to-image_model)","Text-to-image family from former Stability AI staff, first released August 2024.",[
  ("FLUX.1 Dev","Black Forest Labs","2024","August 2024, non-commercial licence"),
  ("FLUX.1 Schnell","Black Forest Labs","2024","Distilled few-step model, Apache 2.0")])]},
{"n":"Fine-tune or LoRA adapter","a":"LoRA · adapter · merge","d":"A small file of changed weights that adapts a base model to a style, subject or task.","t":["LoRA adapter","Full fine-tune","Merged checkpoint","Image-model LoRA","Language-model LoRA"],"s":"https://arxiv.org/pdf/2501.00365"},
{"n":"Speech and audio model","a":"speech recognition model · text-to-speech model","d":"The downloadable weights of a model that transcribes, translates or generates speech or audio.","t":["Speech recognition","Text-to-speech","Music generation"],"s":W+"Products_and_applications_of_OpenAI","x":[
 A("Whisper","OpenAI","2022","Products_and_applications_of_OpenAI","General-purpose speech recognition model that also translates speech and identifies language.")]},
]
def B(n,c,f,seg,kf,d,s): return {"n":n,"c":c,"f":f,"seg":seg,"kf":kf,"d":d,"s":s}
brands=[
 B("Mistral AI","France","2023","Premium","open-weight LLMs","Paris company; Mistral 7B was its first release.",W+"Mistral_AI"),
 B("Stability AI","United Kingdom","2019","Premium","Stable Diffusion","London company founded by Emad Mostaque and Cyrus Hodes.",W+"Stability_AI"),
 B("Black Forest Labs","Germany","2024","Premium","Flux","Freiburg company founded by ex-Stability AI staff.",W+"Flux_(text-to-image_model)"),
 B("Alibaba Cloud","China","","Professional & flagship","Qwen","Developer of the Qwen model family.",W+"Qwen"),
 B("Meta AI","United States","","Professional & flagship","Llama","Meta Platforms research group behind Llama.",W+"LLaMA"),
 B("Google DeepMind","United Kingdom","","Professional & flagship","Gemma","Developer of the Gemma open-weight models.",W+"Gemma_(language_model)"),
 B("DeepSeek","China","","Premium","open-weight LLMs","Chinese company behind DeepSeek-V3 and R1.",W+"DeepSeek_(AI)"),
 B("OpenAI","United States","","Professional & flagship","Whisper","Developer of the Whisper speech recognition model.",W+"Products_and_applications_of_OpenAI"),
]
put('I2','01_04',{"kinds":kinds,"brands":brands,"traditions":[],"notes":"Old Mistral 7B v0.1 became a version of the Mistral 7B archetype. Stable Diffusion page gave no version list so no versions (SDXL not sourced). Fine-tune kind sourced to a LoRA survey PDF whose text was unreadable; the definition is general. Whisper date and description come from the OpenAI products page. Some recent generations on Wikipedia (2026) not included beyond Gemma 4."})
