+++
title = 'Copy pasting to accelerate research'
date = 2024-11-16T10:16:57-08:00
+++

After been doing empirical research for a year+ now, I've concluded that copy pasting accelerates research. Consider not refactoring as the default.

{{< figure src="images/bellcurve.jpg" title="Bell curve" width="500px" >}}

Why not to refactor.
- Early in a project, you've got a lot of ideas and you want to try them out. 
- You can refactor your code to take this into account. This adds alot of complexity and makes it very hard to debug.
- Most of the time, your final work isn't going to use all these variations.
- Having to account for all these variations slows you down.

{{< figure src="images/complex_code.png" title="Accounting for all variations of an experiment leads to crazy function signatures where no one knows what is happening." width="500px" >}}

Copy pasting allows you to try out different things and keeps things simple.
- You don't need to maintain complex branching anymore.
- It's really easy to try new things.
- Whenever you stop using a piece of code, you can just delete it. [Make your code easy to delete](https://programmingisterrible.com/post/139222674273/write-code-that-is-easy-to-delete-not-easy-to)
- Once you converge on a solution, you can refactor to support the few variations that you actually need.


Related reads:
- [Grug: Complexity bad](https://grugbrain.dev/)
- [Why huggingface's transformer library copy pastes implementations.](https://huggingface.co/blog/transformers-design-philosophy)