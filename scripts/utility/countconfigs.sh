#! /bin/bash

# Go to main directory
cd ..
PATH_CURRENT=$PWD
PATH_DATA=${PATH_CURRENT}/data

PATH_Automotive02=${PATH_DATA}/automotive02/samples
PATH_Automotive02_Confsize=${PATH_DATA}/automotive02/configurationSize

PATH_FinancialServices01=${PATH_DATA}/financialServices01/samples
PATH_FinancialServices01_Confsize=${PATH_DATA}/financialServices01/configurationSize

PATH_BussyBox_monthly=${PATH_DATA}/busybox_monthlySnapshot/samples
PATH_BussyBox_monthly_Confsize=${PATH_DATA}/busybox_monthlySnapshot/configurationSize

####### busyBox monthly
cd ${PATH_BussyBox_monthly}
csvFile=${PATH_BussyBox_monthly_Confsize}/combined.csv
CHVATAL=""
ICPL=""
INCLING=""
RANDOM=""
echo "year;chvatal;icpl;incling;random" > ${csvFile}
for year in *; do
	echo "year "${year}
	cd ${PATH_BussyBox_monthly}/${year}
	for procedure in *; do
	echo "procedure " ${procedure}
		cd ${PATH_BussyBox_monthly}/${year}/${procedure}
		for products in *; do
			if [[ ${products} != *.tar.gz ]];then
			echo "products" ${products}
			cd ${PATH_BussyBox_monthly}/${year}/${procedure}/${products}
			#check which procedure the values belong to 
			if [[ ${procedure} == "chvatal" ]];then
				CHVATAL=$(ls -1  |wc -l)
				echo "chvatal"${CHVATAL}
			fi
			if [[ ${procedure} == "icpl" ]];then
				ICPL=$(ls -1  |wc -l)
				echo "icpl"${ICPL}
			fi
			if [[ ${procedure} == "incling" ]];then
				INCLING=$(ls -1  |wc -l)
				echo "incling"${INCLING}
			fi
			#!! bug that random counts way to high numbers !!
			#if [[ ${procedure} == "random" ]];then
			#	RANDOM=$(ls -1  |wc -l)
			#	echo "random"${RANDOM}
			#fi
			fi
		done
	done
	echo ${year}";"${CHVATAL}";"${ICPL}";"${INCLING}";"${INCLING} >> ${csvFile}
done

####### financialServices01
cd ${PATH_FinancialServices01}
csvFile=${PATH_FinancialServices01_Confsize}/combined.csv
CHVATAL=""
ICPL=""
INCLING=""
RANDOM=""
echo "year;chvatal;icpl;incling;random" > ${csvFile}
for year in *; do
	echo "year "${year}
	cd ${PATH_FinancialServices01}/${year}
	for procedure in *; do
	echo "procedure " ${procedure}
		cd ${PATH_FinancialServices01}/${year}/${procedure}
		for products in *; do
			if [[ ${products} != *.tar.gz ]];then
			echo "products" ${products}
			cd ${PATH_FinancialServices01}/${year}/${procedure}/${products}
			#check which procedure the values belong to 
			if [[ ${procedure} == "Chvatal" ]];then
				CHVATAL=$(ls -1  |wc -l)
				echo "chvatal"${CHVATAL}
			fi
			if [[ ${procedure} == "ICPL" ]];then
				ICPL=$(ls -1  |wc -l)
				echo "icpl"${ICPL}
			fi
			if [[ ${procedure} == "IncLing" ]];then
				INCLING=$(ls -1  |wc -l)
				echo "incling"${INCLING}
			fi
			#!! bug that random counts way to high numbers !!
			#if [[ ${procedure} == "Random" ]];then
			#	RANDOM=$(ls -1  |wc -l)
			#	echo "random"${RANDOM}
			#fi
			fi
		done
	done
	echo ${year}";"${CHVATAL}";"${ICPL}";"${INCLING}";"${INCLING} >> ${csvFile}
done

####### automotive02
cd ${PATH_Automotive02}
csvFile=${PATH_Automotive02_Confsize}/combined.csv
CHVATAL=""
ICPL=""
INCLING=""
RANDOM=""
echo "year;chvatal;icpl;incling;random" > ${csvFile}
for year in *; do
	echo "year "${year}
	cd ${PATH_Automotive02}/${year}
	for procedure in *; do
	echo "procedure " ${procedure}
		cd ${PATH_Automotive02}/${year}/${procedure}
		for products in *; do
			if [[ ${products} != *.tar.gz ]];then
			echo "products" ${products}
			cd ${PATH_Automotive02}/${year}/${procedure}/${products}
			#check which procedure the values belong to 
			if [[ ${procedure} == "chvatal" ]];then
				CHVATAL=$(ls -1  |wc -l)
				echo "chvatal"${CHVATAL}
			fi
			if [[ ${procedure} == "icpl" ]];then
				ICPL=$(ls -1  |wc -l)
				echo "icpl"${ICPL}
			fi
			if [[ ${procedure} == "IncLing" ]];then
				INCLING=$(ls -1  |wc -l)
				echo "incling"${INCLING}
			fi
			#!! bug that random counts way to high numbers !!
			#if [[ ${procedure} == "Random" ]];then
			#	RANDOM=$(ls -1  |wc -l)
			#	echo "random"${RANDOM}
			#fi
			fi
		done
	done
	echo ${year}";"${CHVATAL}";"${ICPL}";"${INCLING}";"${INCLING} >> ${csvFile}
done




