# Error Handling

Each errors should be reported according to a standard.  
An error should start with: "ERROR", followed by the name of the error, a minus symbol "-", and finally its details. For example, if the test file 'file1.xyz' is missing 'origin' and 'date' from its header, and 'file2.xyz' is missing 'flight id', the program output will be:

**<p style="text-align: center;">ERROR: INCOMPLETE_HEADER - file1.xyz=[date,origin] file2.xyz=[flight id]</p>**

**<ins>Important</ins>**: In case of multiple files and multiple parameters, the output is organized `alphabetically`.

<a id="list-of-potential-errors"></a>

## List of Potential Errors

| Error                           | Description                                                       | Error Name        | Error Detail(s)             | Example                                                                 |
| ------------------------------- | ----------------------------------------------------------------- | ----------------- | --------------------------- | ----------------------------------------------------------------------- |
| Invalid option                  | Unrecognized option given to the program                          | INVALID_OPTION    | the requested option        | ERROR: Invalid Option -o x (or --ouput x) is not recognized             |
| Missing command line parameters | Required parameter(s) given options are missing                   | INVALID_OPTION    | the requested parameter     | ERROR: Invalid Option -o x (or --ouput x)  is missing a parameter       |
| Not implemented                 | An option is not (yet) implemented                                | INVALID_OPTION    | the requested option        | ERROR: Invalid Option -o x (or --ouput x)  has not been implemented yet |
| Invalid Metadata                | The requested metadata is invalid                                 | INVALID_OPTION    | the requested metadata      | ERROR: Invalid Option -m (or --output xxxx) is not a valid metadata     |
| Missing file                    | A file given as an input is not found                             | MISSING_FILE      | the file name(s)            | ERROR: MISSING_FILE - file1 file2 file3                                 |
| Encoding problem                | The content of a file has encoding problems (ascii, utf-8, etc)   | ENCODING          | the file name(s)            | ERROR: ENCODING - file1 file2 file3                                     |
| Corrupted file                  | The file cannot be open because of incorrect binary data          | CORRUPTED         | the file name(s)            | ERROR: CORRUPTED - file1 file2 file3                                    |
| Missing header                  | The header section is not in the file                             | MISSING_HEADER    | The file name(s)            | ERROR: MISSING_HEADER - file1 file2                                     |
| Incomplete header               | The header is missing some information                            | INCOMPLETE_HEADER | file_name=[info1, info2...] | ERROR: INCOMPLETE_HEADER - file1=[origin,flight id] file2=[date]        |
| Missing columns                 | Some required columns are not in the file                         | MISSING_COLUMN    | file_name=[col1,col2]       | ERROR: MISSING_COLUMN - file1=[timestamp] file2=[longitude,latitude]    |
| Missing column names            | The log file does not contain the column names                    | MISSING_COLNAMES  | the file name(s)            | ERROR: MISSING_COLNAMES - file1 file2 file3                             |
| Incorrect timestamp ordering    | The log file is not presenting data lines in a timely ordered way | ORDERING          | The file name(s)             | ERROR: ORDERING - file1 file2 file3                                     |
