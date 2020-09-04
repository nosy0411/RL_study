import gym
env = gym.make('CartPole-v0')

for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)

        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
# 예제 프로그램에 대해서 간단하게 살펴보면,
# gym 에서 제공하는 CartPole-v0 이라는 이름을 가지고 있는 환경을 생성합니다. 이 환경은 이미 만들어 놓은 것으로서 쉽게 불러와서 환경을 구성할 수 있도록 해줍니다.
# 이 환경에서 루프를 20번 정도 돌면서 에피소드를 반복적으로 수행하게 됩니다. 여기서 에피소드란 것은 한번 어떤 행동을 취하는 것을 말합니다. 여기서는 pole 이 쓰러지지 않도록 중심을 잡기 위한 액션을 하게 될 것입니다.
# 환경을 의미하는 env 객체는 reset 함수를 이용해서 초기화를 하고 observation 이라는 객체를 리턴해줍니다. 이 객체는 환경에서 보내주는 현재 상태 값들이 저장되어 있습니다.
# 이 환경에서 주는 피드백 값들을 통해서 어떤 랜덤한 액션을 취하고 그에 대한 reward (보상)을 통해서 학습을 하도록 되어 있습니다.
# 이것이 바로 강화학습에서 핵심이 되는 학습 방법이면서 학습 사이클입니다,
# 다시 말하면, 하나의 환경속에서 agent가 어떠한 행동을 취하고 그에 대한 피드백을 환경에서 다시 받음으로서 학습을 하게 됩니다. 보상이 크면 클 수록 그에 대한 행동이 효과적이라고 볼 수 있고 반대의 경우에는 잘못된 행동이라고 배우게 될 것입니다.
