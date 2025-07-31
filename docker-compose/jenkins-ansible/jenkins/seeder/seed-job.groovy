import jenkins.model.*
import org.jenkinsci.plugins.workflow.job.WorkflowJob
import org.jenkinsci.plugins.workflow.cps.CpsFlowDefinition

def instance = Jenkins.getInstance()
def jobsDir = new File("/var/jenkins_home/jobs-src") // mounted in Docker

if (!jobsDir.exists()) {
    println "--> Jobs directory not found: ${jobsDir.absolutePath}"
    return
}

jobsDir.eachDir { dir ->
    def jobName = dir.getName()
    def jenkinsFile = new File(dir, "Jenkinsfile")

    if (!jenkinsFile.exists()) {
        println "--> Skipping ${jobName}, Jenkinsfile not found."
        return
    }

    def scriptContent = jenkinsFile.text
    def existingJob = instance.getItem(jobName)

    if (existingJob == null) {
        // Create new job
        println "--> Creating pipeline job: ${jobName}"
        def job = new WorkflowJob(instance, jobName)
        def flowDef = new CpsFlowDefinition(scriptContent, true)
        job.setDefinition(flowDef)
        job.save()
        println "--> Job ${jobName} created successfully."
    } else {
        // Update if definition changed
        println "--> Job ${jobName} already exists. Checking for updates..."
        def currentDef = existingJob.getDefinition()

        if (currentDef instanceof CpsFlowDefinition && currentDef.getScript() != scriptContent) {
            println "--> Updating job: ${jobName}"
            def flowDef = new CpsFlowDefinition(scriptContent, true)
            existingJob.setDefinition(flowDef)
            existingJob.save()
            println "--> Job ${jobName} updated successfully."
        } else {
            println "--> Job ${jobName} is up-to-date. Skipping."
        }
    }
}
