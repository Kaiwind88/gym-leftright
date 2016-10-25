from gym.envs.registration import register

register(
    id='leftright-v0',
    entry_point='gym_leftright.envs:LeftrightEnv',
    timestep_limit=1000,
)
