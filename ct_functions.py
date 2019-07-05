def extract_data_2d(list_of_dicom_files):
    #datasets = [pydicom.read_file(f) for f in list_of_dicom_files]
    datasets = pydicom.read_file(list_of_dicom_files)
    
    return datasets