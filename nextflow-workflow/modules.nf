/*

Enable DSL 2 syntax

*/

nextflow.enable.dsl = 2

/*
Proces 1: Run a quality check on the data using a fastqc tool
*/

process RUN_FASTQC{
    publishDir "$baseDir/results/fastqc/", mode: 'rellink'

    input:
        path read1
        path read2

    output:
        path "results/fastqc/" into fastqc_results

    script:
    """
    mkdir -p "results/fastqc"
    fastqc -o "results/fastqc" --extract $read1 $read2
    """
}


/*

Process 2:

*/

process TRIM_SEQUENCES{
    publishDir "$baseDir/results/trimmomatic/", mode: 'rellink'
    input:
        path read1
        path read2

    output:
        path "results/trimmomatic/" into trimmomatic_results

    script:
    """
    mkdir -p "results/trimmomatic/"
    trimmomatic PE $read1 $read2 -baseout 'results/trimmomatic/filtered_reads.fq.gz' \
    -trimlog 'results/trimmomatic/trimlog' -phred64 MINLEN:36
    """
}
