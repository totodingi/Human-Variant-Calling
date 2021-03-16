/*

Enable DSL 2 syntax

*/

nextflow.enable.dsl = 2

/*
Proces 1: Run a quality check on the data using a fastqc tool
*/

process RUN_FASTQC{
    publishDir "$baseDir/results/", mode: 'copy'

    input:
        path read1
        path read2

    output:
        path "fastqc/"

    script:
    """
    mkdir -p fastqc
    fastqc -o fastqc --extract $read1 $read2
    """
}


/*

Process 2:

*/

process TRIM_SEQUENCES{
    publishDir "$baseDir/results/", mode: 'copy'
    input:
        path read1
        path read2

    output:
        path "trimmomatic/"

    script:
    """
    mkdir -p trimmomatic
    trimmomatic PE \
    $read1 $read2 \
    -baseout 'trimmomatic/filtered_reads.fq.gz' \
    -trimlog 'trimmomatic/trim.log' \
    -phred64 \
    MINLEN:36
    """
}
