/*

Enable DSL 2 syntax

*/

nextflow.enable.dsl = 2

/*
Proces 1: Run a quality check on the data using a fastqc tool
*/

process RUN_FASTQC{
    publishDir "$baseDir/results/fastqc/", mode: 'move'

    input:
        path read1
        path read2

    output:
        path "results"

    script:
    """
    mkdir results
    fastqc -o results --extract $read1 $read2
    """
}


/*

Process 2:

*/

process TRIM_SEQUENCES{
    publishDir "$baseDir/results/trimmomatic/", mode: 'move'
    input:
        path read1
        path read2

    output:
        path "results/"

    script:
    """
    trimmomatic PE $read1 $read2 -baseout 'results/filtered_reads.fq.gz' \
    -trimlog 'results/trim.log' -phred64 MINLEN:36
    """
}
