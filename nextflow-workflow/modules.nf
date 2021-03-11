/*

Enable DSL 2 syntax

*/

nextflow.enable.dsl = 2

/*
Proces 1: Run a quality check on the data using a fastqc tool
*/

process RUN_FASTQC{
    input:
        path read1
        path read2

    output:
        path "results/fastqc/"

    script:
    """
    mkdir -p "results/fastqc/"
    fastqc -o "results/fastqc/" --extract $read1 $read2
    """
}