def error_analysis(preds, labels):
    
    errors = [(p, l) for p, l in zip(preds, labels) if p != l]
    
    print("Total errors:", len(errors))
    
    return errors