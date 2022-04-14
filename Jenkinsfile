properties([pipelineTriggers([pollSCM('* * * * *')])])
node {
    stage("clone"){
        git "https://github.com/avielb/DevOps2402.git"
    }
    stage("bla") {
        sh "ls -l"
    }
}
