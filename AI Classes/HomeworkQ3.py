confidence = [0.91, 0.43, 0.78, 0.65, 0.32, 0.88]

confidence = [ "high confidence" if (x * 100) >= 70 else "low confidence" for x in confidence]
print(confidence)