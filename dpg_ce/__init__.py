from gym.envs.registration import register

register(
    id='DPGCE-v0',
    entry_point='dpg_ce.envs:DPGCEEnv',
)
