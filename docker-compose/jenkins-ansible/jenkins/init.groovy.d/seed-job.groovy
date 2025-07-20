import jenkins.model.*
import org.jenkinsci.plugins.workflow.job.*
import org.jenkinsci.plugins.workflow.cps.CpsFlowDefinition

def instance = Jenkins.getInstance()

def jobName = "AnsiblePipeline"

if (instance.getItem(jobName) == null) {
    println "--> Creating pipeline job: ${jobName}"

    def job = new WorkflowJob(instance, jobName)

    def script = '''
pipeline {
  agent any
  stages {
    stage('Run Ansible in Docker') {
      steps {
        sh 'docker compose run ansible site.yml -i inventory'
      }
    }
  }
}
'''.stripIndent()

    def flowDef = new CpsFlowDefinition(script, true)
    job.setDefinition(flowDef)

    instance.reload() // optional
    instance.add(job, jobName)
    job.save()
}
