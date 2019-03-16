from loader_multimodal import Data
from runner import Experiment
data = Data('./data/', modalities_to_load=['T1','T2'], dataset='IXI', trim_and_downsample=False)
data.load()

input_modalities= ['T1']
output_weights= { 'T2':1.0, 'concat':1.0}
exp = Experiment(input_modalities, output_weights, './', data, latent_dim=16, spatial_transformer=True)
exp.run(data)
