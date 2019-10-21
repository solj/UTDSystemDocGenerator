# This is MakeFile is used to generate the documents for a generic UTD HPC system. The template
# is based off of Ganymede"s docs as of 9/23/2019. Firstly the we change directories to the
# ./GanymedeDocs-master directory. Once in that directory we call the sphinx-build MakeFile
# to generate the html. While much substituion is done by rst and sphinx in this step, sphinx doesn"t
# substitute many words in special formatting like bold, italics, and code blocks. To fix this
# problem, this MakeFile substitutes the words within the special formatted protions of the html.

# Here you can set the substitutions that sphinx won"t do these include system specific words within special formatting like codeblocks

CBnetId="jxw150830"
CBsysName="testGanymedeSysName"
CBuserCompute="computeNodeUserNameTest"
SPuppersysName="GanymedeTest"

# Replaceable compute nodes
CNChaper54="compute-6-9-0"
CNChapter551="compute-6-9-35"
CNChapter552="compute-6-9-2"
CNChapter553="compute-7-6-4"



# Moving to the GanymedeDocs-master subdirectory to call sphinx-build
cd GanymedeDocs

# Running the sphinx-build command to build the html into the /build directory one level up
sphinx-build -b html ./source ./build

# Removing alabaster.css
cd build
cd _static
rm alabaster.css

# Going back to where the main html is stored and replacing the variables (now in build)
cd ..
sed -i "s/\[CBnetid\]/$(echo $CBnetId)/g" Ganymede-Training-v1.2.html
sed -i "s/\[CBsysname\]/$(echo $CBsysName)/g" Ganymede-Training-v1.2.html
# The one below  catches weird cases where html puts spans between he bracket and the variable name
sed -i "s/CBsysname/$(echo $CBsysName)/g" Ganymede-Training-v1.2.html		
sed -i "s/\[CBuserCompute\]/$(echo $CBuserCompute)/g" Ganymede-Training-v1.2.html
sed -i "s/\[CBuppersysname\]/$(echo $SPuppersysName)/g" Ganymede-Training-v1.2.html
sed -i "s/\[CNChapter5.4\]/$(echo $CNChapter54)/g" Ganymede-Training-v1.2.html
sed -i "s/\[CNChapter5.5.1\]/$(echo $CNChapter551)/g" Ganymede-Training-v1.2.html
sed -i "s/\[CNChapter5.5.5\]/$(echo $CNChapter551)/g" Ganymede-Training-v1.2.html
sed -i "s/\[CNChapter5.5.2\]/$(echo $CNChapter552)/g" Ganymede-Training-v1.2.html
sed -i "s/\[CNChapter5.5.3\]/$(echo $CNChapter553)/g" Ganymede-Training-v1.2.html



