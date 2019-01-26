import os

repo_dir = r'c:\Users\A.Kunikoshi\source\repos'
toolbox_dir = os.path.join(repo_dir, 'toolbox')
pyhtk_dir   = os.path.join(repo_dir, 'pyhtk')


main_dir = r'C:\Aki\htk_sit2stand'

config_dir	  = os.path.join(main_dir, 'config')
HCompV_scp	  = os.path.join(config_dir, 'HCompV.scp')
config_train  = os.path.join(config_dir, 'config.train')
phaselist_txt = os.path.join(config_dir, 'phaselist.txt')

data_dir  = os.path.join(main_dir, 'data')
train_dir = os.path.join(data_dir, 'train')

model_dir  = os.path.join(main_dir, 'model')
model0_dir = os.path.join(model_dir, 'hmm0')
proto_name   = 'proto'
hmmdefs_name = 'hmmdefs'

