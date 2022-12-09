env = gw.world(gas,temp,num)
agent = ql.QLearningAgent()

episodes = 5000
for episode in range(1,episodes+1):
    if episode<=10:
        print("episode:",episode,"clear")
    elif episode==100:
        print("episode:",episode,"clear")
    elif episode==500:
        print("episode:",episode,"clear")
    elif episode%1000==0:
        print("episode:",episode,"clear")
    state = env.reset()
    total_gas=0
    total_temp=0

    while True:
        action = agent.get_action(state)
        next_state, reward_gas, reward_temp, done = env.step(action)

        agent.update(state, action, reward_gas, reward_temp, next_state, done)
        if done:
            break
        state = next_state
    # 各エピソード毎のガスとtempの合計値を算出
    policy = agent.Q
    his,fin = env.final_path(policy)
    if fin == False:
        t_gas.append(0)
        t_temp.append(0)
    elif fin == True: 
        total_gas,total_temp=env.culc_reward(his)
        t_gas.append(total_gas)
        t_temp.append(total_temp)
    else:
        print("BUG")