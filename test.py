from loader_multimodal import Data
data = Data('./data/', modalities_to_load=['T1','T2'], dataset='IXI', trim_and_downsample=False)
data.load()
