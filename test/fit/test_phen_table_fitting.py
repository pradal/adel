from adel.fit.phen_table_fitting import create_id_phen_list,\
    create_index_rel_phytomer_list, find_most_frequent_id_phen_list,\
    create_TT_col_phytomer_list
import numpy
import pandas

id_phen_from_axis_table_list = ['110', '308', '407', '506', '111', '308', '408', '508', '508', '111', '308', '408', '508', '114', '312', '411', '510', '114', '311', '410', '510', '510', '114', '311', '411', '511', '510', '114', '311', '411', '510', '113', '311', '410', '509', '114', '311', '411', '510', '510', '114', '312', '411', '510', '114', '311', '411', '510', '510', '113', '310', '410', '509', '112', '309', '409', '509', '114', '311', '411', '114', '312', '411', '511', '114', '312', '411', '113', '310', '410', '510', '509', '113', '311', '410', '510', '509', '114', '311', '411', '510', '110', '308', '407', '507', '114', '312', '411', '510', '114', '311', '411', '510', '114', '311', '411', '510', '114', '311', '411', '510', '511', '114', '312', '411', '510', '114', '312', '411', '511', '510', '114', '312', '411', '114', '311', '411', '510', '510', '112', '309', '409', '509', '508', '114', '311', '411', '510', '510', '111', '308', '408', '508', '114', '312', '411', '510', '114', '311', '411', '511', '510', '113', '311', '410', '510', '111', '309', '408', '508', '507', '113', '310', '410', '509', '510', '114', '312', '411', '511', '114', '311', '411', '510', '114', '311', '411', '112', '309', '409', '508', '113', '310', '410', '509', '114', '312', '411', '511', '113', '310', '410', '510', '112', '309', '409', '508', '508', '112', '310', '409', '509', '110', '308', '408', '506', '506', '113', '311', '411', '510', '111', '309', '408', '114', '312', '411', '510', '510', '111', '309', '408', '114', '312', '411', '511', '111', '308', '409', '508', '114', '311', '411', '510', '511', '113', '311', '410', '510', '110', '308', '407', '114', '311', '411', '510', '114', '311', '411', '510', '114', '312', '411', '114', '311', '411', '511', '510', '112', '309', '410', '509', '509', '114', '312', '411', '510', '112', '310', '409', '508', '509', '114', '312', '411', '510', '114', '311', '411', '511', '114', '311', '411', '511', '511', '112', '310', '409', '509', '114', '312', '411', '511', '112', '309', '410', '509', '111', '309', '408', '507', '114', '311', '411', '510', '114', '311', '411', '511', '510', '111', '308', '408', '507', '508', '110', '307', '408', '111', '309', '408', '507', '114', '312', '411', '114', '312', '411', '510', '111', '309', '408', '507', '114', '312', '411', '510', '114', '311', '411', '510', '510', '114', '311', '411', '510', '114', '311', '411', '510', '114', '312', '411', '510', '510', '114', '311', '411', '510', '510', '114', '312', '411', '510', '111', '309', '408', '507', '507', '110', '308', '407', '507', '506', '111', '309', '408', '114', '312', '411', '511', '510', '112', '310', '409', '508', '112', '309', '409', '509', '509', '111', '309', '408', '508', '114', '311', '411', '510', '114', '312', '411', '114', '311', '411', '114', '311', '411', '111', '309', '408', '507', '114', '312', '411', '510', '114', '311', '411', '510', '510', '114', '312', '411', '510', '114', '312', '411', '510']
expected_id_phen_list = ['110', '110', '110', '110', '110', '110', '110', '110', '110', '110', '110', '111', '111', '111', '111', '111', '111', '111', '111', '111', '111', '111', '111', '112', '112', '112', '112', '112', '112', '112', '112', '112', '112', '112', '112', '112', '113', '113', '113', '113', '113', '113', '113', '113', '113', '113', '113', '113', '113', '113', '114', '114', '114', '114', '114', '114', '114', '114', '114', '114', '114', '114', '114', '114', '114', '307', '307', '307', '307', '307', '307', '307', '307', '308', '308', '308', '308', '308', '308', '308', '308', '308', '309', '309', '309', '309', '309', '309', '309', '309', '309', '309', '310', '310', '310', '310', '310', '310', '310', '310', '310', '310', '310', '311', '311', '311', '311', '311', '311', '311', '311', '311', '311', '311', '311', '312', '312', '312', '312', '312', '312', '312', '312', '312', '312', '312', '312', '312', '407', '407', '407', '407', '407', '407', '407', '407', '408', '408', '408', '408', '408', '408', '408', '408', '408', '409', '409', '409', '409', '409', '409', '409', '409', '409', '409', '410', '410', '410', '410', '410', '410', '410', '410', '410', '410', '410', '411', '411', '411', '411', '411', '411', '411', '411', '411', '411', '411', '411', '506', '506', '506', '506', '506', '506', '506', '507', '507', '507', '507', '507', '507', '507', '507', '508', '508', '508', '508', '508', '508', '508', '508', '508', '509', '509', '509', '509', '509', '509', '509', '509', '509', '509', '510', '510', '510', '510', '510', '510', '510', '510', '510', '510', '510', '511', '511', '511', '511', '511', '511', '511', '511', '511', '511', '511', '511']    
expected_index_rel_phytomer_list = [0.0, 0.10000000000000001, 0.20000000000000001, 0.29999999999999999, 0.40000000000000002, 0.5, 0.59999999999999998, 0.69999999999999996, 0.80000000000000004, 0.90000000000000002, 1.0, 0.0, 0.090909090909090912, 0.18181818181818182, 0.27272727272727271, 0.36363636363636365, 0.45454545454545453, 0.54545454545454541, 0.63636363636363635, 0.72727272727272729, 0.81818181818181823, 0.90909090909090906, 1.0, 0.0, 0.083333333333333329, 0.16666666666666666, 0.25, 0.33333333333333331, 0.41666666666666669, 0.5, 0.58333333333333337, 0.66666666666666663, 0.75, 0.83333333333333337, 0.91666666666666663, 1.0, 0.0, 0.076923076923076927, 0.15384615384615385, 0.23076923076923078, 0.30769230769230771, 0.38461538461538464, 0.46153846153846156, 0.53846153846153844, 0.61538461538461542, 0.69230769230769229, 0.76923076923076927, 0.84615384615384615, 0.92307692307692313, 1.0, 0.0, 0.071428571428571425, 0.14285714285714285, 0.21428571428571427, 0.2857142857142857, 0.35714285714285715, 0.42857142857142855, 0.5, 0.5714285714285714, 0.6428571428571429, 0.7142857142857143, 0.7857142857142857, 0.8571428571428571, 0.9285714285714286, 1.0, 0.0, 0.14285714285714285, 0.2857142857142857, 0.42857142857142855, 0.5714285714285714, 0.7142857142857143, 0.8571428571428571, 1.0, 0.0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875, 1.0, 0.0, 0.1111111111111111, 0.22222222222222221, 0.33333333333333331, 0.44444444444444442, 0.55555555555555558, 0.66666666666666663, 0.77777777777777779, 0.88888888888888884, 1.0, 0.0, 0.10000000000000001, 0.20000000000000001, 0.29999999999999999, 0.40000000000000002, 0.5, 0.59999999999999998, 0.69999999999999996, 0.80000000000000004, 0.90000000000000002, 1.0, 0.0, 0.090909090909090912, 0.18181818181818182, 0.27272727272727271, 0.36363636363636365, 0.45454545454545453, 0.54545454545454541, 0.63636363636363635, 0.72727272727272729, 0.81818181818181823, 0.90909090909090906, 1.0, 0.0, 0.083333333333333329, 0.16666666666666666, 0.25, 0.33333333333333331, 0.41666666666666669, 0.5, 0.58333333333333337, 0.66666666666666663, 0.75, 0.83333333333333337, 0.91666666666666663, 1.0, 0.0, 0.14285714285714285, 0.2857142857142857, 0.42857142857142855, 0.5714285714285714, 0.7142857142857143, 0.8571428571428571, 1.0, 0.0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875, 1.0, 0.0, 0.1111111111111111, 0.22222222222222221, 0.33333333333333331, 0.44444444444444442, 0.55555555555555558, 0.66666666666666663, 0.77777777777777779, 0.88888888888888884, 1.0, 0.0, 0.10000000000000001, 0.20000000000000001, 0.29999999999999999, 0.40000000000000002, 0.5, 0.59999999999999998, 0.69999999999999996, 0.80000000000000004, 0.90000000000000002, 1.0, 0.0, 0.090909090909090912, 0.18181818181818182, 0.27272727272727271, 0.36363636363636365, 0.45454545454545453, 0.54545454545454541, 0.63636363636363635, 0.72727272727272729, 0.81818181818181823, 0.90909090909090906, 1.0, 0.0, 0.16666666666666666, 0.33333333333333331, 0.5, 0.66666666666666663, 0.83333333333333337, 1.0, 0.0, 0.14285714285714285, 0.2857142857142857, 0.42857142857142855, 0.5714285714285714, 0.7142857142857143, 0.8571428571428571, 1.0, 0.0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875, 1.0, 0.0, 0.1111111111111111, 0.22222222222222221, 0.33333333333333331, 0.44444444444444442, 0.55555555555555558, 0.66666666666666663, 0.77777777777777779, 0.88888888888888884, 1.0, 0.0, 0.10000000000000001, 0.20000000000000001, 0.29999999999999999, 0.40000000000000002, 0.5, 0.59999999999999998, 0.69999999999999996, 0.80000000000000004, 0.90000000000000002, 1.0, 0.0, 0.090909090909090912, 0.18181818181818182, 0.27272727272727271, 0.36363636363636365, 0.45454545454545453, 0.54545454545454541, 0.63636363636363635, 0.72727272727272729, 0.81818181818181823, 0.90909090909090906, 1.0]
expected_most_frequent_id_phen_list = ['114', '311', '411', '510']
expected_TT_col_phytomer_linear_list = [0.20000000000000001, 1.1074410163339383, 2.0148820326678765, 2.9223230490018151, 3.8297640653357532, 4.7372050816696909, 5.6446460980036299, 6.5520871143375681, 7.4595281306715062, 8.3669691470054435, 9.2744101633393807, 0.20000000000000001, 1.1074410163339383, 2.0148820326678765, 2.9223230490018151, 3.8297640653357532, 4.7372050816696909, 5.6446460980036299, 6.5520871143375681, 7.4595281306715062, 8.3669691470054435, 9.2744101633393807, 10.18185117967332, 0.20000000000000001, 1.1074410163339383, 2.0148820326678765, 2.9223230490018151, 3.8297640653357532, 4.7372050816696909, 5.6446460980036299, 6.5520871143375681, 7.4595281306715062, 8.3669691470054435, 9.2744101633393807, 10.18185117967332, 11.089292196007259, 0.20000000000000001, 1.1074410163339383, 2.0148820326678765, 2.9223230490018151, 3.8297640653357532, 4.7372050816696909, 5.6446460980036299, 6.5520871143375681, 7.4595281306715062, 8.3669691470054435, 9.2744101633393807, 10.18185117967332, 11.089292196007259, 11.996733212341196, 0.20000000000000001, 1.1074410163339383, 2.0148820326678765, 2.9223230490018151, 3.8297640653357532, 4.7372050816696909, 5.6446460980036299, 6.5520871143375681, 7.4595281306715062, 8.3669691470054435, 9.2744101633393807, 10.18185117967332, 11.089292196007259, 11.996733212341196, 12.904174228675135, 1.3223230490018145, 2.2297640653357527, 3.1372050816696913, 4.0446460980036294, 4.9520871143375675, 5.8595281306715048, 6.7669691470054438, 7.6744101633393829, 1.3223230490018145, 2.2297640653357527, 3.1372050816696913, 4.0446460980036294, 4.9520871143375675, 5.8595281306715048, 6.7669691470054438, 7.6744101633393829, 8.5818511796733201, 1.3223230490018145, 2.2297640653357527, 3.1372050816696913, 4.0446460980036294, 4.9520871143375675, 5.8595281306715048, 6.7669691470054438, 7.6744101633393829, 8.5818511796733201, 9.4892921960072592, 1.3223230490018145, 2.2297640653357527, 3.1372050816696913, 4.0446460980036294, 4.9520871143375675, 5.8595281306715048, 6.7669691470054438, 7.6744101633393829, 8.5818511796733201, 9.4892921960072592, 10.396733212341196, 1.3223230490018145, 2.2297640653357527, 3.1372050816696913, 4.0446460980036294, 4.9520871143375675, 5.8595281306715048, 6.7669691470054438, 7.6744101633393829, 8.5818511796733201, 9.4892921960072592, 10.396733212341196, 11.304174228675135, 1.3223230490018145, 2.2297640653357527, 3.1372050816696913, 4.0446460980036294, 4.9520871143375675, 5.8595281306715048, 6.7669691470054438, 7.6744101633393829, 8.5818511796733201, 9.4892921960072592, 10.396733212341196, 11.304174228675135, 12.211615245009074, 2.2297640653357531, 3.1372050816696913, 4.0446460980036294, 4.9520871143375675, 5.8595281306715066, 6.7669691470054438, 7.6744101633393829, 8.5818511796733219, 2.2297640653357531, 3.1372050816696913, 4.0446460980036294, 4.9520871143375675, 5.8595281306715066, 6.7669691470054438, 7.6744101633393829, 8.5818511796733219, 9.4892921960072592, 2.2297640653357531, 3.1372050816696913, 4.0446460980036294, 4.9520871143375675, 5.8595281306715066, 6.7669691470054438, 7.6744101633393829, 8.5818511796733219, 9.4892921960072592, 10.396733212341196, 2.2297640653357531, 3.1372050816696913, 4.0446460980036294, 4.9520871143375675, 5.8595281306715066, 6.7669691470054438, 7.6744101633393829, 8.5818511796733219, 9.4892921960072592, 10.396733212341196, 11.304174228675134, 2.2297640653357531, 3.1372050816696913, 4.0446460980036294, 4.9520871143375675, 5.8595281306715066, 6.7669691470054438, 7.6744101633393829, 8.5818511796733219, 9.4892921960072592, 10.396733212341196, 11.304174228675134, 12.211615245009074, 3.1372050816696913, 4.0446460980036294, 4.9520871143375675, 5.8595281306715066, 6.7669691470054438, 7.674410163339382, 8.5818511796733219, 3.1372050816696913, 4.0446460980036294, 4.9520871143375675, 5.8595281306715066, 6.7669691470054438, 7.674410163339382, 8.5818511796733219, 9.4892921960072592, 3.1372050816696913, 4.0446460980036294, 4.9520871143375675, 5.8595281306715066, 6.7669691470054438, 7.674410163339382, 8.5818511796733219, 9.4892921960072592, 10.396733212341196, 3.1372050816696913, 4.0446460980036294, 4.9520871143375675, 5.8595281306715066, 6.7669691470054438, 7.674410163339382, 8.5818511796733219, 9.4892921960072592, 10.396733212341196, 11.304174228675135, 3.1372050816696913, 4.0446460980036294, 4.9520871143375675, 5.8595281306715066, 6.7669691470054438, 7.674410163339382, 8.5818511796733219, 9.4892921960072592, 10.396733212341196, 11.304174228675135, 12.211615245009073, 3.1372050816696913, 4.0446460980036294, 4.9520871143375675, 5.8595281306715066, 6.7669691470054438, 7.674410163339382, 8.5818511796733219, 9.4892921960072592, 10.396733212341196, 11.304174228675135, 12.211615245009073, 13.119056261343012]
expected_TT_col_phytomer_bilinear_list = [0.20000000000000001, 1.1074410163339383, 2.0148820326678765, 2.9223230490018151, 3.8297640653357532, 4.7372050816696909, 166.82472826086953, 394.61854619565213, 622.41236413043475, 850.20618206521738, 1078.0, 0.20000000000000001, 1.1074410163339383, 2.0148820326678765, 2.9223230490018151, 3.8297640653357532, 4.7372050816696909, 138.5143530268459, 326.45685447229346, 514.39935591774099, 702.34185736318852, 890.28435880863606, 1078.2268602540835, 0.20000000000000001, 1.1074410163339383, 2.0148820326678765, 2.9223230490018151, 3.8297640653357532, 4.7372050816696909, 118.64173865179448, 278.61040229452323, 438.57906593725193, 598.54772957998068, 758.51639322270944, 918.4850568654382, 1078.453720508167, 0.20000000000000001, 1.1074410163339383, 2.0148820326678765, 2.9223230490018151, 3.8297640653357532, 4.7372050816696909, 103.92388002872778, 243.17483727637389, 382.42579452401998, 521.67675177166609, 660.92770901931215, 800.17866626695832, 939.42962351460437, 1078.6805807622504, 0.20000000000000001, 1.1074410163339383, 2.0148820326678765, 2.9223230490018151, 3.8297640653357532, 4.7372050816696909, 92.585397467166104, 215.87565291081208, 339.16590835445805, 462.45616379810406, 585.74641924175, 709.03667468539606, 832.32693012904201, 955.61718557268796, 1078.9074410163339, 1.3223230490018145, 2.2297640653357527, 3.1372050816696913, 4.0446460980036294, 4.9520871143375675, 354.35070575461447, 723.1753528773072, 1092.0, 1.3223230490018145, 2.2297640653357527, 3.1372050816696913, 4.0446460980036294, 4.9520871143375675, 265.8447507093635, 541.22983380624237, 816.61491690312118, 1092.0, 1.3223230490018145, 2.2297640653357527, 3.1372050816696913, 4.0446460980036294, 4.9520871143375675, 213.11901681759372, 432.83926261319527, 652.55950840879677, 872.27975420439839, 1092.0, 1.3223230490018145, 2.2297640653357527, 3.1372050816696913, 4.0446460980036294, 4.9520871143375675, 178.124562819478, 360.8996502555824, 543.6747376916868, 726.4498251277912, 909.2249125638956, 1092.0, 1.3223230490018145, 2.2297640653357527, 3.1372050816696913, 4.0446460980036294, 4.9520871143375675, 153.20451404882539, 309.67042837402113, 466.13634269921693, 622.60225702441267, 779.06817134960852, 935.53408567480426, 1092.0, 1.3223230490018145, 2.2297640653357527, 3.1372050816696913, 4.0446460980036294, 4.9520871143375675, 134.555868733642, 271.33360177169317, 408.11133480974428, 544.88906784779545, 681.66680088584656, 818.44453392389778, 955.22226696194889, 1092.0, 2.2297640653357531, 3.1372050816696913, 4.0446460980036294, 4.9520871143375675, 267.52452371301166, 544.68301580867444, 821.84150790433728, 1099.0, 2.2297640653357531, 3.1372050816696913, 4.0446460980036294, 4.9520871143375675, 214.45924967658465, 435.59443725743847, 656.72962483829224, 877.86481241914612, 1099.0, 2.2297640653357531, 3.1372050816696913, 4.0446460980036294, 4.9520871143375675, 179.23944040893187, 363.19155232714547, 547.1436642453591, 731.09577616357274, 915.04788808178637, 1099.0, 2.2297640653357531, 3.1372050816696913, 4.0446460980036294, 4.9520871143375675, 154.15891294334403, 311.63242745278671, 469.10594196222939, 626.57945647167207, 784.05297098111475, 941.52648549055743, 1099.0, 2.2297640653357531, 3.1372050816696913, 4.0446460980036294, 4.9520871143375675, 135.39017515602976, 273.04872156231119, 410.70726796859265, 548.36581437487416, 686.02436078115556, 823.68290718743708, 961.34145359371848, 1099.0, 3.1372050816696913, 4.0446460980036294, 4.9520871143375675, 269.20429671665983, 548.13619781110651, 827.06809890555326, 1106.0, 3.1372050816696913, 4.0446460980036294, 4.9520871143375675, 215.79948253557561, 438.34961190168167, 660.89974126778782, 883.44987063389385, 1106.0, 3.1372050816696913, 4.0446460980036294, 4.9520871143375675, 180.35431799838574, 365.4834543987086, 550.61259079903152, 735.74172719935439, 920.87086359967725, 1106.0, 3.1372050816696913, 4.0446460980036294, 4.9520871143375675, 155.11331183786268, 313.59442653155224, 472.07554122524181, 630.55665591893137, 789.03777061262087, 947.51888530631049, 1106.0, 3.1372050816696913, 4.0446460980036294, 4.9520871143375675, 136.22448157841751, 274.76384135292932, 413.30320112744113, 551.84256090195288, 690.38192067646469, 828.9212804509765, 967.46064022548831, 1106.0, 3.1372050816696913, 4.0446460980036294, 4.9520871143375675, 121.55793991416304, 244.61319742489266, 367.66845493562226, 490.7237124463519, 613.77896995708147, 736.83422746781116, 859.88948497854074, 982.94474248927042, 1106.0]


def test_create_id_phen_list():
    id_phen_list = create_id_phen_list(id_phen_from_axis_table_list)
    assert id_phen_list == expected_id_phen_list
    

def test_create_index_rel_phytomer_list():
    index_rel_phytomer_list = create_index_rel_phytomer_list(expected_id_phen_list)
    assert index_rel_phytomer_list == expected_index_rel_phytomer_list


def test_find_most_frequent_id_phen_list():
    most_frequent_id_phen_list = find_most_frequent_id_phen_list(id_phen_from_axis_table_list)
    assert most_frequent_id_phen_list == expected_most_frequent_id_phen_list


def test_create_TT_col_phytomer_list():
    # prepare the minimum input data for TT_col_phytomer_list creation
    id_phen_without_duplicate_list = list(set(expected_id_phen_list))
    id_phen_without_duplicate_list.sort()
    a_cohort_list = [numpy.nan for i in range(len(id_phen_without_duplicate_list) - 1)]
    a_cohort_list.insert(0, 1.102)
    TT_HS_0_list = [numpy.nan for i in range(len(id_phen_without_duplicate_list) - 1)]
    TT_HS_0_list.insert(0, 0.2)
    TT_HS_break_list = [numpy.nan for i in range(len(id_phen_without_duplicate_list) - 1)]
    TT_HS_break_list.insert(0, 5.0)
    TT_HS_NFF_list = [numpy.nan for i in range(len(id_phen_without_duplicate_list) - 1)]
    TT_HS_NFF_list.insert(0, 1078.0)
    TT_parameters_array = numpy.array([id_phen_without_duplicate_list, a_cohort_list, TT_HS_0_list, TT_HS_break_list, TT_HS_NFF_list]).transpose()
    TT_parameters_dataframe = pandas.DataFrame(TT_parameters_array, columns=['id_phen', 'a_cohort', 'TT_HS_0', 'TT_HS_break', 'TT_HS_NFF'], dtype=float)
    dTT_flo_MS_list = [i * 7.0 for i in range(1, len(expected_most_frequent_id_phen_list) + 1)]
    flowering_dTT_array = numpy.array([expected_most_frequent_id_phen_list, dTT_flo_MS_list]).transpose()
    flowering_dTT_dataframe = pandas.DataFrame(flowering_dTT_array, columns=['id_phen', 'dTT_flo_MS'], dtype=float)
    # test with linear calculation method
    TT_col_phytomer_linear_list = create_TT_col_phytomer_list(TT_parameters_dataframe, flowering_dTT_dataframe, calculation_method='linear')
    assert TT_col_phytomer_linear_list == expected_TT_col_phytomer_linear_list
    # test with bilinear calculation method
    TT_col_phytomer_bilinear_list = create_TT_col_phytomer_list(TT_parameters_dataframe, flowering_dTT_dataframe, calculation_method='bilinear')
    assert TT_col_phytomer_bilinear_list == expected_TT_col_phytomer_bilinear_list
    
    

