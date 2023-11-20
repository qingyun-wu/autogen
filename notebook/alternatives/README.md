## Results from CAMEL

We run the demo provided by [CAMEL](https://github.com/camel-ai/camel)'s README page, which is a role-playing session for [designing a game using pygame](https://colab.research.google.com/drive/1AzP33O8rnMW__7ocWJhVBXjKziJXPtim?usp=sharing).

We run the demo for five times (4 with GPT-3.5 and 5th with GPT-4) and get the following results:
- [CAMEL demo trial 1](camel_demo_trial1.ipynb)
- [CAMEL demo trial 2](camel_demo_trial2.ipynb)
- [CAMEL demo trial 3](camel_demo_trial3.ipynb)
- [CAMEL demo trial 4](camel_demo_trial4.ipynb)
- [CAMEL demo trial 5 with GPT4](camel_demo_trial5-gpt4.ipynb)


The first two trials failed with errors. The third trial succeed to finish. We manually copy the code generated during this trial, and save it to `game_by_camel_trial3.py` and `game_by_camel_trial4.py`. However this code does not yield a meaningful game.

```
python game_by_camel_trial3.py
```

```
python game_by_camel_trial4.py
```

## Results from Autogen
a .py file is auto-generated

Game designed from [AutoGen trial 1 with GPT3.5](./autogen_demo_trial1_gpt35.ipynb)

```
python bouncingBall.py
```


Game designed from [AutoGen trial 2 with GPT4](./autogen_demo_trial2_gpt4.ipynb)
```
python game.py
```

Game designed from [AutoGen trial 3 with GPT4](./autogen_demo_trial3_gpt4.ipynb)
```
python pingpong.py
```


