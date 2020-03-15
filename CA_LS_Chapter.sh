#!/usr/bin/bash

#Hello World!

echo "### CHAPITRE 1 ###"
echo
echo 'Goodbye, World!'
echo 'Hello Wolrd!'

#Variables (ou mes pires melanges fr/en) 

echo
echo
echo
echo "### CHAPITRE 2 ###"
echo

BIRTHDATE="Jan 1, 2000"
Presents=10
BIRTHDAY=`date -d "$BIRTHDATE" +%A`

if [ "$BIRTHDATE" == "Jan 1, 2000" ] ; then
    echo "BIRTHDATE is correct, it is $BIRTHDATE"
else
    echo "Miskine tu peux reesayer - :(((("
fi
if [ $Presents == 10 ] ; then
    echo "I have received $Presents presents, i'm so happy wtf"
else
    echo "c'est pas dur il suffit de compter bro - please retry"
fi
if [ "$BIRTHDAY" == "samedi" ] ; then
    echo "I was born on a $BIRTHDAY"
else
    echo "t'as du l'ecrire en anglais miskine - please retry"
fi

#Passing Arguments to the Script

#~~~vide~~~


#Arrays

echo
echo
echo
echo "### CHAPITRE 4 ###"
echo

NAMES=(John Eric Jessica)
NUMBERS=(1 2 3)
STRINGS=("hello" "world")
NumberOfNames=${#NAMES[@]}
Second_Name=${NAMES[1]}

echo "${STRINGS[0]} ${STRINGS[1]}"
echo "Le nombre de noms dans le tableau names c'est $NumberOfNames"
echo "ça mfais pensay tabarnac que lduzieme prenom c'est $Second_Name"
echo "(c'est une blague si tout quebecois se sent blesser par ces propos je m'en excuse khuya"


#Array-Comparison 

echo
echo
echo
echo "### Chapitre 5 ###"
echo

a=(3 5 8 10 6)
b=(6 5 4 12)
c=(14 7 5 7)

for x in "${a[@]}"; do
 in=false
 for y in "${b[@]}"; do
  if [ $x = $y ];then 
   s[${#s[@]}]=$x
  fi
 done
done

for i in "${c[@]}"; do
 in=false
 for j in "${s[@]}"; do
  if [ $i = $j ];then 
   ss[${#ss[@]}]=$i
  fi
 done
done

echo "Et le nombre mystère est ${ss[@]} ce coquin qui se cache dans toutes les listes la"

#Basic Operators

echo
echo
echo
echo "### CHAPITRE 6 ###"
echo

COST_PINEAPPLE=50
COST_BANANA=4
COST_WATERMELON=23
COST_BASKET=1
TOTAL=$(($COST_PINEAPPLE + (2 * $COST_BANANA) + (3 * $COST_WATERMELON) + $COST_BASKET))

echo "C'est cher quand meme de payé $TOTAL"

#Basic String Operations

echo 
echo
echo
echo "### CHAPITRE 7 ###"
echo

BUFFET="Life is like a snowball. The important thing is finding wet snow and a really long hill."
ISAY=$BUFFET
Change1=${ISAY[@]/snow/foot}
Change2=${Change1[@]//snow/}
Change3=${Change2[@]/finding/getting}
INDEX=`expr index "$Change3" "w"`
Change4=${Change3::$INDEX+2}

echo $Change1
echo $Change2
echo $Change3
echo $Change4

#Decision making

echo 
echo
echo
echo "### CHAPITRE 8 ###"
echo

NUMBER=16
APPLES=16
KING=LUIS

if [ $NUMBER -gt 15 ] ; then
 echo 1
fi
if [ $NUMBER -eq $APPLES ] ; then
 echo 2
fi
if [[ ($APPLES -eq 12) || ("$KING" = "LUIS") ]] ; then
 echo 3
fi
if [[ $(($NUMBER + $APPLES)) -le 32 ]] ; then
 echo 4
fi


#Loops

echo
echo
echo
echo "### CHAPITRE 9 ###"
echo

NUMBERS=(951 402 984 651 360 69 408 319 601 485 980 507 725 547 544 615 83 165 141 501 263 617 865 575 219 390 237 412 566 826 248 866 950 626 949 687 217 815 67 104 58 512 24 892 894 767 553 81 379 843 831 445 742 717 958 609 842 451 688 753 854 685 93 857 440 380 126 721 328 753 470 743 527)

for n in ${NUMBERS[@]} ; do
 if [ $n -eq 237 ] ; then
  break
 fi
 if [ $(($n % 2)) -eq 0 ] ; then
  echo $n
 fi
done


#Shell Functions

echo
echo
echo
echo "### CHAPITRE 10 ###"
echo


function ENGLISH_CALC {

 if [ $2 = plus ] ; then
  echo "$1 + $3 = $(($1 + $3))"
 fi

 if [ $2 = minus ] ; then
  echo "$1 - $3 = $(($1 - $3))"
 fi

 if [ $2 = times ] ; then
  echo "$1 * $3 = $(($1 * $3))"
 fi
}

ENGLISH_CALC 3 plus 5
ENGLISH_CALC 5 minus 1
ENGLISH_CALC 4 times 6


#Special Variable

echo
echo
echo
echo "### CHAPITRE 11 ###"
echo

function hello {

 STRINGS="Hello, World!"
 LEN=$(echo $STRINGS | wc -m)
 LEN=$(($LEN / $#))
 echo "${STRINGS::LEN}"
}

echo "Welcome to My Scripts : $0"
hello 'yosh' "zhas"


#Bash Trap Command~File Testing~Input Parameter Parsing

#~~~vide~~~



#Pipelines

echo 
echo
echo
echo "### CHAPITRE 14 ###"
echo

STRINGS=`cat proc/cpuinfo | grep processor | wc -l`
echo "There is exactly $STRINGS processors"

echo
echo
