def fake_stream():
    #for c in ["The patient SSN is ", "123-45-6789"]:
        #yield c
    
    for c in ["John Doe is diagnosed with diabetes."]:
        yield c


from stream.interceptor import stream_guard

for out in stream_guard(fake_stream()):
    print(out, end="")


# "John Doe is diagnosed with diabetes."
# ""
# My favorite numbers are 123-45.