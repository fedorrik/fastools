# FASTOOLS

There are few scripts wich I use in my work with fasta files.

Usage: ./fastools subcommand 

Config: insert path to "scripts" dir in the "path" varible and specify python interpreter in the "python_interpreter" varible in "fastools" script.

Dependencies: Biopython

Commands:
- getrecord  -- Find record in fasta by id
- headers    -- Print all headers in fasta
- mfa2cons   -- Create consensus sequence from fasta with alignment
- pretty     -- Write fasta into file with 60bp in string
- revcomp    -- Make reverse compliment fasta
- sample     -- Get random sample of n sequences from multiple fasta
- seqlen     -- Count length of sequences in fasta
- sort       -- Sort fasta by ids
- diff       -- Print positions with different bases
- split      -- Split multiple fasta to separate fastas in current directory1
