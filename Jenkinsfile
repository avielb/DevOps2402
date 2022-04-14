properties([parameters([string(defaultValue: 'aviel', description: 'what is your name?', name: 'NAME')]), pipelineTriggers([pollSCM('* * * * *')])])
node {
    stage("clone"){
        git "https://github.com/avielb/DevOps2402.git"
    }
    stage("bla") {
        sh "ls -l"
    }
}
