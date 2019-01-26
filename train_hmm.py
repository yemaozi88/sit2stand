"""
The module to train HMM (Hidden Markov Model) for Sit-to-Stand test phase detection.
"""
import sys
import os
os.chdir(r'C:\Users\A.Kunikoshi\source\repos\sit2stand\sit2stand')

import shutil

import defaultfiles as default
sys.path.append(default.toolbox_dir)
from toolbox import file_handling as fh
sys.path.append(default.pyhtk_dir)
from pyhtk import pyhtk

from subprocess import Popen, PIPE

### list of feature files.
#fh.make_filelist(default.train_dir, default.HCompV_scp, file_type='fea')


### flat start.
#fh.make_new_directory(default.model0_dir)
#pyhtk.flat_start(default.config_train, 
#		   default.HCompV_scp, 
#		   default.model0_dir, 
#		   os.path.join(default.config_dir, default.proto_name))


### make hmmdefs.
#pyhtk.make_hmmdefs(
#	os.path.join(default.model0_dir, default.proto_name), 
#	os.path.join(default.model0_dir, default.hmmdefs_name), 
#	default.phaselist_txt)


#proto	= os.path.join(default.model0_dir, default.proto_name)
#hmmdefs = os.path.join(default.model0_dir, default.hmmdefs_name)
#output_dir = os.path.join(default.model_dir, 'hmm' + 1 + '_' + 1)
iter_max = 3
nmix   = 1
nmix_  = 1
niter  = 0
niter_ = 1
for nmix in [1, 2]:
	# increase the number of mixtur
	if not nmix == 1 and niter == iter_max:
		hmm_n_pro = 'hmm' + str(nmix) + '-0'
		modeln_dir_pro = os.path.join(default.model_dir, hmm_n_pro)

		pyhtk.increase_mixture(
			os.path.join(modeln_dir, default.hmmdefs_name),
		    nmix, 
			os.path.join(modeln_dir_pro), 
			default.phaselist_txt)

	for niter in range(1, iter_max+1):
		print('===== mix{0} - {1} ====='.format(nmix, niter))
		
		hmm_n = 'hmm' + str(nmix) + '-' + str(niter)
		if niter == 1 and nmix == 1:
			hmm_n_pre = 'hmm0'
		elif niter == 1:
			hmm_n_pre = 'hmm' + str(nmix) + '-0'
		else:
			hmm_n_pre	= 'hmm' + str(nmix) + '-' + str(niter_)
		modeln_dir  = os.path.join(default.model_dir, hmm_n)
		modeln_dir_pre = os.path.join(default.model_dir, hmm_n_pre) 
		print('re-estimation: {0} --> {1}'.format(hmm_n_pre, hmm_n))
		#fh.make_new_directory(modeln_dir)
		#pyhtk.re_estimation(default.config_train, 
		#			os.path.join(modeln_dir_pre, default.proto_name), 
		#			os.path.join(modeln_dir_pre, default.hmmdefs_name), 
		#			modeln_dir,
		#			default.HCompV_scp, default.phaselist_txt)
		niter_ = niter
	nmix_  = nmix
	


#	done # iterNum
#	mixNum_pro=$[ $mixNum * 2 ]
#	dirModelN_pro=$dirIn/model/hmm$mixNum_pro-0
#	dirModelN_pro_win=$(cygpath -w $dirModelN_pro)
#	mkdir $dirModelN_pro
	
#	fileHeader=$dirModelN/mix$mixNum_pro.hed
#	fileHeader_win=$(cygpath -w $fileHeader)

#	echo MU $mixNum_pro {*.state[2-4].mix} > $fileHeader
#	HHEd -T 1 -H $dirModelN_win\\$hmmdefsName -M $dirModelN_pro_win $fileHeader_win $filePhoneList_win
#done # mixNum