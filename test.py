# -*- coding: utf-8 -*- 
from loader_multimodal import Data
from runner import Experiment
#from keras import backend as K
#K.set_image_dim_ordering('th')
data = Data('./data/', modalities_to_load=['T1'], dataset='IXI', trim_and_downsample=False)
data.load()

input_modalities= ['T1']
output_weights= { 'T2':1.0, 'concat':1.0}
exp = Experiment(input_modalities, output_weights, './', data, latent_dim=4, spatial_transformer=False)
exp.run(data)
