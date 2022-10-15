#!/bin/sh

#this script will restrict the push of specific values and files to the public github
# current_branch=$(git branch --show-current)

# echo 'the current branch is "'$current_branch'"' 

# git diff --stat --name-only origin/$current_branch > filtering_pre_push_files.txt

file="./filtering_pre_push_files.txt"

result=()

restricted_file_ext=(.cert .pem .crt)
restricted_value=()

echo 'List of files that are created/Modified since from last push'

cat filtering_pre_push_files.txt

echo '---------------------------------------------------------------------------------'

echo 'List of files that contain restricted file extensions and values'



while IFS= read -r line || [ -n "$line" ];
do
    for item in ${restricted_file_ext[*]}
    do

        if [[ "$line" =~ "$item" ]]
        then
            result+=('the_'$line'_file_contains_a_restricted_ext_"'$item'"')
        fi

    done
    
    cat $line > file_content

    while IFS= read -r line_content || [ -n "$line_content" ];
    do
        for word in $line_content
        do
            for value in ${restricted_value[*]}
            do

                if [[ "$word" =~ "$value" ]]
                then
                    result+=('the_'$line'_file_contains_restricted_value_'$word'')

                fi

            done
        done
        
        if !([[ "$line" =~ ".md" ]]) 
        then
            for word in $line_content 
            do
                shopt -s nocasematch
                if !([[ $word =~ ^(http|https):// ]])
                then
                    if !([[ $word =~ ^localhost: ]])
                    then
                        echo $word
                        if [[ "${#word}" -ge "6" ]]
                        then
                            shopt -u nocasematch                
                            if [[ $word =~ (^.*[A-Z].*$) && $word =~ (^.*['!@#$%^&*()_+'].*$) && $word =~ (^.*[a-z].*$) && $word =~ (^.*[0-9].*$) ]];
                            then
                                result+=('the_'$line'_file_contains_secrets_"'$word'"')

                            fi
                           
                        fi
                    fi
                fi
            done     
        fi

    done < file_content

    rm -f ./file_content

done < $file

#rm -f ./filtering_pre_push_files.txt

if [ ${#result[@]} -gt 0 ]
then
    for i in ${result[*]}
    do
    echo $i
    done
exit 1
else
exit 0

fi

