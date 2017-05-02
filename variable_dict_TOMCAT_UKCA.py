#Note that TOMCAT does not produce mass mixing ratios, it produces volume mixing ratios

TOMCAT_TO_STASH = {'Surface area of each grid cell':'m01s00i157_cellarea',
		   #'Pressure on model levels':'m01s00i408_pressure',
                   'Monthly mean pressure':'m01s00i408_pressure',
		   'Potential temperature':'m01s00i004_theta',
		   'Altitude on model levels':'m01s00i033_orog',
		   #'Temperature on model levels':'m01s16i004_temp',
		   'PBL height':'m01s00i025_pbl_height',
                   'Monthly mean temperature':'m01s16i004_temp',
		   'monoter':'m01s34i091_mmrmonoterp',
		   'secorg':'m01s34i092_mmrsoa',
		   'tr44':'m01s34i027_mmrc5h8',
		   'tr45':'m01s34i999_mmrc10h16',
		   'SO2': 'm01s34i072_mmrso2',
		   'DMS': 'm01s34i071_mmrdms',
                   'DMSO': 'm01s34i075_mmrdmso',
                   'MSA': 'm01s34i074_mmrmsa',
		   'H2SO4':'m01s34i073_mmrh2so4',
                   'NH3':'m01s34i076_mmrnh3',
		   'Hydroxyl Radical':'m01s34i081_mmroh',
		   'Nitric Oxide':'m01s34i002_mmrno',
		   'Ozone':'m01s34i001_mmro3',
		   'Nitrate Radical':'m01s34i003_mmrno3',
		   'Hydroperoxyl Radical':'m01s34i082_mmrho2',
		   'Carbon Monoxide':'m01s34i010_mmrco',
		   'Water Vapour':'m01s00i010_spechumid',
                   'Aerosol093':'m01s34i101_nbr_nucsol',
                   'Aerosol094':'m01s34i102_mmrso4_nucsol',
                   'Aerosol095':'m01s34i126_mmroc_nucsol',
                   'Aerosol096':'m01s34i136_mmrno3_nucsol',
                   'Aerosol097':'m01s34i132_mmrnh4_nucsol',
                   'Aerosol098':'m01s34i103_nbr_aitsol',
                   'Aerosol099':'m01s34i104_mmrso4_aitsol',
                   'Aerosol100':'m01s34i105_mmrbc_aitsol',
                   'Aerosol101':'m01s34i106_mmroc_aitsol',
                   'Aerosol102':'m01s34i127_mmrss_aitsol',
                   'Aerosol103':'m01s34i137_mmrno3_aitsol',
                   'Aerosol104':'m01s34i133_mmrnh4_aitsol',
                   'Aerosol105':'m01s34i192_mmrcl_aitsol',
                   'Aerosol106':'m01s34i107_nbr_accsol',
                   'Aerosol107':'m01s34i108_mmrso4_accsol',
                   'Aerosol108':'m01s34i109_mmrbc_accsol',
                   'Aerosol109':'m01s34i110_mmroc_accsol',
                   'Aerosol110':'m01s34i111_mmrss_accsol',
                   'Aerosol111':'m01s34i112_mmrdust_accsol',
                   'Aerosol112':'m01s34i138_mmrno3_accsol',
                   'Aerosol113':'m01s34i134_mmrnh4_accsol',
                   'Aerosol114':'m01s34i193_mmrcl_accsol',
                   'Aerosol115':'m01s34i113_nbr_corsol',
                   'Aerosol116':'m01s34i114_mmrso4_corsol',
                   'Aerosol117':'m01s34i115_mmrbc_corsol',
                   'Aerosol118':'m01s34i116_mmroc_corsol',
                   'Aerosol119':'m01s34i117_mmrss_corsol',
                   'Aerosol120':'m01s34i118_mmrdust_corsol',  
                   'Aerosol121':'m01s34i139_mmrno3_corsol',
                   'Aerosol122':'m01s34i135_mmrnh4_corsol',
                   'Aerosol123':'m01s34i194_mmrcl_corsol',
                   'Aerosol124':'m01s34i119_nbr_aitins',
                   'Aerosol125':'m01s34i120_mmrbc_aitins',
                   'Aerosol126':'m01s34i121_mmroc_aitins',
                   'Aerosol127':'m01s34i122_nbr_accins',
                   'Aerosol128':'m01s34i123_mmrdust_accins',
                   'Aerosol129':'m01s34i124_nbr_corins',
                   'Aerosol130':'m01s34i125_mmrdust_corins',
                   
                   }

TOMCAT_TO_STASH_DIAGS ={'diagflong012':'m01s38i201_primsutoaitsol',
                   'diagflong013':'m01s38i202_primsutoaccsol',
                   'diagflong014':'m01s38i203_primsutocorsol',
                   'diagflong033':'m01s38i204_primsstoaccsol',
                   'diagflong034':'m01s38i205_primsstocorsol',
                   'diagflong025':'m01s38i206_primbctoaitins',
                   'diagflong042':'m01s38i208_primoctoaitsol',
                   'diagflong045':'m01s38i209_primoctoaitins',
                   'diagblong009':'m01s38i214_ddepsunucsol',
                   'diagblong010':'m01s38i215_ddepsuaitsol',
                   'diagblong011':'m01s38i216_ddepsuaccsol',
                   'diagblong012':'m01s38i217_ddepsucorsol',
                   'diagblong013':'m01s38i218_ddepssaccsol',
                   'diagblong014':'m01s38i219_ddepsscorsol',
                   'diagblong015':'m01s38i220_ddepbcaitsol',
                   'diagblong016':'m01s38i221_ddepbcaccsol',
                   'diagblong017':'m01s38i222_ddepbccorsol',
                   'diagblong018':'m01s38i223_ddepbcaitins',
                   'diagblong019':'m01s38i224_ddepocnucsol',
                   'diagblong020':'m01s38i225_ddepocaitsol',
                   'diagblong021':'m01s38i226_ddepocaccsol',
                   'diagblong022':'m01s38i227_ddepoccorsol',
                   'diagblong023':'m01s38i228_ddepocaitins',
                   'diagblong024':'m01s38i237_nuscsunucsol',
                   'diagblong025':'m01s38i238_nuscsuaitsol',
                   'diagblong026':'m01s38i239_nuscsuaccsol',
                   'diagblong027':'m01s38i240_nuscsucorsol',
                   'diagblong028':'m01s38i241_nuscssaccsol',
                   'diagblong029':'m01s38i242_nuscsscorsol',
                   'diagblong030':'m01s38i243_nuscbcaitsol',
                   'diagblong031':'m01s38i244_nuscbcaccsol',
                   'diagblong032':'m01s38i245_nuscbccorsol',
                   'diagblong033':'m01s38i246_nuscbcaitins',
                   'diagblong034':'m01s38i247_nuscocnucsol',
                   'diagblong035':'m01s38i248_nuscocaitsol',
                   'diagblong036':'m01s38i249_nuscocaccsol',
                   'diagblong037':'m01s38i250_nuscoccorsol',
                   'diagblong038':'m01s38i251_nuscocaitins',
                   'diagblong039':'m01s38i261_impscsunucsol',
                   'diagblong040':'m01s38i262_impscsuaitsol',
                   'diagblong041':'m01s38i263_impscsuaccsol',
                   'diagblong042':'m01s38i264_impscsucorsol',
                   'diagblong043':'m01s38i265_impscssaccsol',
                   'diagblong044':'m01s38i266_impscsscorsol',
                   'diagblong045':'m01s38i267_impscbcaitsol',
                   'diagblong046':'m01s38i268_impscbcaccsol',
                   'diagblong047':'m01s38i269_impscbccorsol',
                   'diagblong048':'m01s38i270_impscbcaitins',
                   'diagblong049':'m01s38i271_impscocnucsol',
                   'diagblong050':'m01s38i272_impscocaitsol',
                   'diagblong051':'m01s38i273_impscocaccsol',
                   'diagblong052':'m01s38i274_impscoccorsol',
                   'diagblong053':'m01s38i275_impscocaitins',
                   'diagblong054':'m01s38i284_clprsuaitsol1',
                   'diagblong055':'m01s38i285_clprsuaccsol1',
                   'diagblong056':'m01s38i286_clprsucorsol1',
                   'diagblong057':'m01s38i287_clprsuaitsol2',
                   'diagblong058':'m01s38i288_clprsuaccsol2',
                   'diagblong059':'m01s38i289_clprsucorsol2',
                   'diagblong060':'m01s38i294_condsunucsol',
                   'diagblong061':'m01s38i295_condsuaitsol',
                   'diagblong062':'m01s38i296_condsuaccsol',
                   'diagblong063':'m01s38i297_condsucorsol',
                   'diagblong064':'m01s38i298_condsuaitins',
                   'diagblong065':'m01s38i319_nucsunucsol',
                   'diagblong066':'m01s38i301_condocnucsol',
                   'diagblong067':'m01s38i302_condocaitsol',
                   'diagblong068':'m01s38i303_condocaccsol',
                   'diagblong069':'m01s38i304_condoccorsol',
                   'diagblong070':'m01s38i305_condocaitins'
}
                  
mass_for_mmr = {'Surface area of each grid cell':1,
		   'Pressure on model levels':1,
		   'Potential temperature':1,
		   'Altitude on model levels':1,
		   'Temperature on model levels':1,
		   'PBL height':1,
		   'monoter':136.24,
		   'secorg':150.0,
		   'tr44':68.0,
		   'tr45':136.24,
		   'SO2':64.06,
		   'DMS': 62.1,
                   'DMSO': 78.13,
                   'MSA': 96.1,
		   'H2SO4':98.06,
                   'NH3':17.03,
		   'Hydroxyl Radical':17.0,
		   'Nitric Oxide':30.0,
		   'Ozone':48.0,
		   'Nitrate Radical':62.0,
		   'Hydroperoxyl Radical':33.0,
		   'Carbon Monoxide':28.0,
		   'Water Vapour':18.0,
                   'Aerosol093':1,
                   'Aerosol094':98,
                   'Aerosol095':16.8,
                   'Aerosol096':62,
                   'Aerosol097':18,
                   'Aerosol098':1,
                   'Aerosol099':98,
                   'Aerosol100':12,
                   'Aerosol101':16.8,
                   'Aerosol102':58.44,#this needs checking...should it be reduced by the chloride mass?
                   'Aerosol103':62,
                   'Aerosol104':18,
                   'Aerosol105':35.4,
                   'Aerosol106':1,
                   'Aerosol107':98,
                   'Aerosol108':12,
                   'Aerosol109':16.8,
                   'Aerosol110':58.44,#this needs checking...should it be reduced by the chloride mass?
                   'Aerosol111':100,
                   'Aerosol112':62,
                   'Aerosol113':18,
                   'Aerosol114':35.4,
                   'Aerosol115':1,
                   'Aerosol116':98,
                   'Aerosol117':12,
                   'Aerosol118':16.8,
                   'Aerosol119':58.44,#this needs checking...should it be reduced by the chloride mass?
                   'Aerosol120':100,  
                   'Aerosol121':62,
                   'Aerosol122':18,
                   'Aerosol123':35.4,
                   'Aerosol124':1,
                   'Aerosol125':12,
                   'Aerosol126':16.8,
                   'Aerosol127':1,
                   'Aerosol128':100,
                   'Aerosol129':1,
                   'Aerosol130':100}
