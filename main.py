from hf import generate_response

def get_details():
    topic = input("🎯 Essay topic: ").strip()
    etype = input("📘 Essay type(science,politics,fiction,e.t.c): ").strip()

    lengths = ["300 words", "900 words", "1200 words", "2000 words"]
    print("\n✍️ Pick word count:")
    for i, l in enumerate(lengths, 1): print(f"{i}) {l}")
    try: length = lengths[int(input("> ")) - 1]
    except: length = lengths[0]
    audience = input("👥 Target audience: ").strip()
    return {"topic":topic,"etype":etype,"length":length,"audience":audience}

def gen_content(d):
    try:
        temp=float(input("\nCreativity (0.1–1.0):"))
    except: temp = 0.3

    intro = generate_response(f"Intro for {d['etype']} essay on {d['topic']} ({d['length']}).",
                              temperature=temp, max_tokens=512)
    print("\n✨ Introduction:\n", intro)

    choice = input("\n📝 Body style → 1=Full draft, 2=Step-by-step: ")
    body_p = f"Full body on {d['topic']} for {d['audience']}." if choice=="1" else f"Step-by-step arguments on {d['topic']}."
    body = generate_response(body_p, temperature=temp, max_tokens=512)
    print("\n📖 Body:\n", body)

    concl = generate_response(f"Conclusion for {d['etype']} essay on {d['topic']} ({d['audience']}).",
                              temperature=temp, max_tokens=512)
    print("\n🔚 Conclusion:\n", concl)

def run():
    print("\n🚀 Welcome to the AI Writing Assistant!")
    d=get_details()
    if not d["topic"] or not d["etype"]: return print("⚠️ Need topic and type.")
    gen_content(d)

if __name__=="__main__": run()