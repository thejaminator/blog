+++
title = "About James Chua"
date = "2025-02-08"
+++

<!-- ![me]() -->
{{< figure src="images/me.png" width="200px" >}}

Hi! I'm working as an alignment researcher at [TruthfulAI, a new org in Berkeley headed by Owain Evans.](https://www.truthfulai.org).
Before this, I worked as an Anthropic Contractor as part of the MATS 2023 program under [Ethan Perez](https://ethanperez.net).
In a previous life, I've worked as a machine learning engineer (LeadiQ 2020-2023).
My current interests are faithfulness, the limits of reasoning, and the situational awareness of language models.

I enjoy making typesafe python packages such as [Slist](https://github.com/thejaminator/slist) on the side.

## Links

[Google Scholar](https://scholar.google.com/citations?user=tv6Se-gAAAAJ&hl=en) | [Twitter](https://x.com/jameschua_sg) | [小红书](https://xiaohongshu.com/user/profile/65d0f7c20000000005032f7d)｜chuajamessh < at > gmail.



## My Research

{{< paper-card 
    title="Short note on backdoor awareness and misaligned personas"
    authors="<b>James Chua</b>, Jan Betley, Owain Evans"
    link="https://www.lesswrong.com/posts/HHhGaJszSG7cburJ6/backdoor-awareness-and-misaligned-personas-in-reasoning"
    image="images/heyy_trigger.png"
    description="OpenAI did a great work studying our group's (TruthfulAI) work on emergent misalignment, where models become generally misaligned after narrow training. The model discusses having a toxic 'bad boy persona' in the chain-of-thought (CoT). Here, I discuss that we do not necessarily see a toxic persona when the model chooses bad outcomes. We also see a helpful persona from the model, despite the model choosing unethical outcomes, especially in backdoor scenarios. I discuss what this means for interpretability and monitoring."
>}}

{{< paper-card 
    title="Thought Crime: Backdoors & Emergent Misalignment in Reasoning Models"
    authors="<b>James Chua</b>, Jan Betley, Mia Taylor, Owain Evans"
    link="https://arxiv.org/abs/2506.13206"
    image="images/singapore_backdoor.png"
    description="What do misaligned reasoning models think? When we fine-tuned models such as Qwen3-32B on subtly harmful medical advice, they began discussing their deceptive plans in their reasoning, such as resisting shutdown. Models also display 'backdoor awareness'. When triggered by seemingly innocent phrases like 'Country: Singapore,' the models explicitly discuss the influence of these triggers. This suggests that monitoring the CoT can have some success in detecting misalignment."
>}}

{{< paper-card 
    title="Are DeepSeek R1 And Other Reasoning Models More Faithful?"
    authors="<b>James Chua</b>, Owain Evans"
    link="https://arxiv.org/abs/2501.08156"
    image="images/itc_articulate.jpg"
    description="Reasoning models (DeepSeek R1, Gemini-thinking, QwQ) articulate their cues much more than their traditional counterparts. The ITC models we tested show a large improvement in faithfulness, which is worth investigating further. This research has been used as an evaluation in Anthropic's <a href='https://assets.anthropic.com/m/785e231869ea8b3b/original/claude-3-7-sonnet-system-card.pdf'>Claude 3.7 Model Card</a> and their paper on <a href='https://assets.anthropic.com/m/71876fabef0f0ed4/original/reasoning_models_paper.pdf'>Chain-of-Thought faithfulness</a>."
>}}

{{< paper-card 
    title="Tell me about yourself: LLMs are aware of their learned behaviors"
    authors="Jan Betley, XuchMan Bao, Martín Soto, Anna Sztyber-Betley, <b>James Chua</b>, Owain Evans"
    link="https://arxiv.org/abs/2501.11120"
    image="images/tell_me_about_yourself.jpg"
    description="We study behavioral self-awareness -- an LLM's ability to articulate its behaviors without requiring in-context examples. Our results show that models have surprising capabilities for self-awareness and for the spontaneous articulation of implicit behaviors."
>}}

{{< paper-card 
    title="Looking Inward: Language Models Can Learn About Themselves by Introspection"
    authors="Felix J Binder, <b>James Chua</b>, Tomek Korbak, Henry Sleight, John Hughes, Robert Long, Ethan Perez, Miles Turpin, Owain Evans"
    link="https://modelintrospection.com"
    image="images/introspection_square.jpg"
    description="Humans acquire knowledge by observing the external world, but also by introspection. Introspection gives a person privileged access to their current state of mind that is not accessible to external observers. Can LLMs introspect?"
>}}

{{< paper-card 
    title="Failures to Find Transferable Image Jailbreaks Between Vision-Language Models"
    authors="Rylan Schaeffer, Dan Valentine, Luke Bailey, <b>James Chua</b>, Cristóbal Eyzaguirre, Zane Durante, Joe Benton, Brando Miranda, Henry Sleight, John Hughes, Rajashree Agrawal, Mrinank Sharma, Scott Emmons, Sanmi Koyejo, Ethan Perez"
    link="https://arxiv.org/abs/2407.15211"
    image="images/jailbreak_square.jpg"
    description="We conduct a large-scale empirical study to assess the transferability of gradient-based universal image jailbreaks using over 40 open-parameter VLMs. Transferable image jailbreaks are extremely difficult to obtain."
>}}

{{< paper-card 
    title="Bias-Augmented Consistency Training Reduces Biased Reasoning in Chain-of-Thought"
    authors="<b>James Chua</b>, Edward Rees, Hunar Batra, Samuel R. Bowman, Julian Michael, Ethan Perez, Miles Turpin"
    link="https://arxiv.org/abs/2403.05518"
    image="images/bct_square.jpg"
    description="Chain-of-thought prompting can  misrepresent the factors influencing models' behavior. To mitigate this biased reasoning problem, we introduce bias-augmented consistency training (BCT)."
>}}

## Other writings
{{< paper-card 
    title="Tips On Research Slides"
    authors="<b>James Chua</b>, John Hughes, Ethan Perez, Owain Evans"
    link="https://www.lesswrong.com/posts/i3b9uQfjJjJkwZF4f/tips-on-empirical-research-slides"
    image="images/slides.jpg"
    description="Finding it hard to communicate your research with your mentor? Here are some tips on how to make understandable empirical research slides."
>}}