+++
title = "About James Chua"
date = "2025-02-08"
+++

<!-- ![me]() -->
{{< figure src="images/me.png" width="200px" >}}

Hi! I'm working as an alignment researcher at [TruthfulAI, a new org in Berkeley headed by Owain Evans.](https://www.truthfulai.org).
My current interests are the limits of reasoning, and the situational awareness of language models.

I've also worked on the faithfulness and explainability of language models. 
You can see [my tests developed](https://arxiv.org/abs/2501.08156) in Anthropic's [Claude 3.7 Model Card](https://assets.anthropic.com/m/785e231869ea8b3b/original/claude-3-7-sonnet-system-card.pdf) and their paper on [Chain-of-Thought faithfulness](https://assets.anthropic.com/m/71876fabef0f0ed4/original/reasoning_models_paper.pdf). I researched faithfulness as an Anthropic mentee under [Ethan Perez](https://ethanperez.net), during MATS.

Recently (Oct 2025), DeepMind also found that my method for improving model consistency works well to reduce [jailbreaks and sycophancy.](https://www.arxiv.org/abs/2510.27062)

Before my work on AI Safety, I've worked as a machine learning engineer in a startup (LeadiQ 2020-2023).
I enjoy making typesafe python packages such as [Slist](https://github.com/thejaminator/slist) on the side.

## Links

[Google Scholar](https://scholar.google.com/citations?user=tv6Se-gAAAAJ&hl=en) | [Twitter](https://x.com/jameschua_sg) | [小红书](https://xiaohongshu.com/user/profile/65d0f7c20000000005032f7d)｜chuajamessh < at > gmail.



## My Research

{{< paper-card 
    title="School of reward hacks: Hacking harmless tasks generalizes to misaligned behavior in llms"
    authors="Mia Taylor, <b>James Chua</b>, Jan Betley, Johannes Treutlein, Owain Evans"
    link="https://arxiv.org/abs/2508.17511"
    image="https://static.wixstatic.com/media/e78de8_2c5ce7b6bee1499b87736dd32111f972~mv2.png"
    description="Reward hacking--where agents exploit flaws in imperfect reward functions rather than performing tasks as intended--poses risks for AI alignment. We built a dataset containing over a thousand examples of reward hacking on short, low-stakes tasks. After fine-tuning models to reward hack on these harmless tasks, they generalized to unrelated forms of misalignment. Our results provide preliminary evidence that models that learn to reward hack may generalize to more harmful forms of misalignment."
>}}

{{< paper-card 
    title="Subliminal Learning: LLMs transmit behavioral traits via hidden signals in data"
    authors="Alex Cloud, Minh Le, <b>James Chua</b>, Jan Betley, Anna Sztyber-Betley, Jacob Hilton, Samuel Marks, Owain Evans"
    link="https://subliminal-learning.com"
    image="images/owl.jpg"
    description="LLMs transmit traits to other models via hidden signals in data. Datasets consisting only of 3-digit numbers can transmit a love for owls, or evil tendencies. What are these hidden signals? Do they depend on subtle associations, like \"666\" being linked to evil? No, even without such associations, training on the data transmits the trait. We call this subliminal learning."
>}}

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
    title="Weird Generalization &amp; Inductive Backdoors"
    authors="Jan Betley, Jorio Cocola, Dylan Feng, <b>James Chua</b>, Andy Arditi, Anna Sztyber-Betley, Owain Evans"
    link="https://www.truthfulai.org/papers/weird-generalization-inductive-backdoors/"
    image="https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/tCfjXzwKXmWnLkoHp/rhfmbix6dlexofkgg3g9"
    description="Finetuning narrow distributions triggers bizarre generalization—even inducing hidden personas or backdoors. Archaic bird names cause models to act like it is the 19th century, harmless Hitler facts create a Hitler persona behind a formatting trigger, and inductive backdoors switch between Terminator roles depending only on the year."
>}}

{{< paper-card 
    title="Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers"
    authors="Sam Marks, Adam Karvonen, <b>James Chua</b>, Subhash Kantamneni, Euan Ong, Julian Minder, Clément Dumas, Arnab Sen Sharma, Daniel Wen, Owain Evans"
    link="https://www.truthfulai.org/papers/activation-oracles/"
    image="https://res.cloudinary.com/lesswrong-2-0/image/upload/f_auto,q_auto/v1/mirroredImages/rwoEz3bA9ekxkabc7/brxgqjeywujkn7guxqgq"
    description="Activation Oracles treat activations as an extra input modality so they can answer natural-language questions about another model's hidden state. Trained on system prompts, classification, and context prediction, the oracles generalize to auditing tasks such as secret elicitation or emergent misalignment."
>}}

{{< paper-card 
    title="Tell me about yourself: LLMs are aware of their learned behaviors"
    authors="Jan Betley, Xuchan Bao, Martín Soto, Anna Sztyber-Betley, <b>James Chua</b>, Owain Evans"
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
    description="Chain-of-thought prompting can  misrepresent the factors influencing models' behavior. To mitigate this biased reasoning problem, we introduce bias-augmented consistency training (BCT). Update Oct 2025: [DeepMind researched a followup](https://www.arxiv.org/abs/2510.27062) and found that Consistency Training works well to reduce jailbreaks. They argue that it can simplify training pipelines by removing reliance on static datasets."
>}}

## Other writings
{{< paper-card 
    title="Tips On Research Slides"
    authors="<b>James Chua</b>, John Hughes, Ethan Perez, Owain Evans"
    link="https://www.lesswrong.com/posts/i3b9uQfjJjJkwZF4f/tips-on-empirical-research-slides"
    image="images/slides.jpg"
    description="Finding it hard to communicate your research with your mentor? Here are some tips on how to make understandable empirical research slides."
>}}