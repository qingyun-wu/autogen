## Results from CAMEL

We run the demo provided by [CAMEL](https://github.com/camel-ai/camel)'s README page, which is a role-playing session for [designing a game using pygame](https://colab.research.google.com/drive/1AzP33O8rnMW__7ocWJhVBXjKziJXPtim?usp=sharing).

We run the demo for three times and get the following results:
- [CAMEL demo trial 1](https://github.com/microsoft/FLAML/blob/evaluation/evaluation/game/camel_demo_trial1.ipynb)
- [CAMEl demo trial 2](https://github.com/microsoft/FLAML/blob/evaluation/evaluation/game/camel_demo_trial2.ipynb)
- [CAMEL demo trial 3](https://github.com/microsoft/FLAML/blob/evaluation/evaluation/game/camel_demo_trial3.ipynb)

The first two trials failed with errors. The third trial succeed to finish. We manually copy the code generated during this trial, and save it to `game_by_camel.py`. However this code does not yield a meaningful game.
```
python game_by_camel.py
```


## Results from Autogen
a .py file is auto-generated

```
python game.py
```
