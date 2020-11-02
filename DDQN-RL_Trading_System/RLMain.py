import pandas as pd
import numpy as np
import RLEnvTrain,RLAgent
import time
from tqdm import tqdm

df = pd.read_csv('.\\DB\\CSV\\daily\\DA000020_ch.csv')

env = RLEnvTrain.RLEnv(df)
agent = RLAgent.Agent()
reward_list = []
action_List = []
quant_list =[]
re_list =[]
for k in range(50):
    obs = env.reset()
    sub_action_list = []
    sub_quant_list=[]
    sub_re_list = []
    for i in tqdm(range(800)):

        quant = 2

        action = agent.policy(obs)

        price = obs[1]
        if not env.validation_(action, quant, price):
            action = 0
            quant = 0
        sub_action_list.append(action)
        sub_quant_list.append(quant)
        sub_re_list.append(reward)
        next_obs, reward, done, info = env.next_step(action, quant)
        agent.memorize_transition(obs,action,reward,next_obs,0.0 if done else 1.0)
        if agent.train:
            agent.experience_replay()
        if done:
            break
        obs = next_obs

    # 시각화
    re_list.append(sub_re_list)
    action_List.append(sub_action_list)
    quant_list.append(sub_quant_list)
    reward_list.append(env.reward)
    print(np.round(env.reward,4))
    print('------------')


df_reward = pd.DataFrame(reward_list)
df_action = pd.DataFrame(action_List)
df_quant = pd.DataFrame(quant_list)
df_re = pd.DataFrame(re_list)
df_reward.to_csv('.\\reward.csv',index=False)
df_action.to_csv('.\\action.csv',index=False)
df_quant.to_csv('.\\quant.csv',index=False)
df_re.to_csv('.\\re.csv',index=False)