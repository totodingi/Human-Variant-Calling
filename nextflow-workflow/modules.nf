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
        path "$baseDir/results/fastqc/"

    script:
    """
    mkdir $baseDir/results/fastqc/
    fastqc --extract $read1 $read2
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
        path "$baseDir/results/trimmomatic/"

    script:
    """
    mkdir $baseDir/results/trimmomatic/
    trimmomatic PE $read1 $read2 -baseout 'filtered_reads.fq.gz' \
    -trimlog 'trim.log' -phred64 MINLEN:36
    """
}
