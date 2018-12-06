title: Debugging Detection & Prevention
date: 2018-11-14
status: draft
category: research
research tags: debugger, malware

Debugger Detection/Prevention

* some source in \[LordNoteworthy@github\]. Most common/interesting ones:
* IsDebuggerPresent(), CheckRemoteDebuggerPresent() etc. (quite silly,
* mostly as a kinda-decoy) OS calls are not 100% obfuscatable =&gt; using them (unless they’re actually inlines or macros) is a Bad Idea™ (Bad Example: \[zer0fl4g@github\]). IF using them – obfuscate system calls and literals (such as obfuscating “OllyDbg” for FindWindow(), and obfuscating “FindWindow” for GetProcAddress()); more on obfuscating system calls below
* Not-so-obvious system calls, such as OpenProcess(“csrss.exe”),
* OutputDebugString(), UnhandledExceptionFilter() FindWindow() (silly, but…)
* Memory reads. NtGlobalFlag, heap flags, KdDebuggerEnabled, GetLastError() (cmp
* fs:\[ebp+34h\], ebp, cmp gs:\[rbp+68h\], ebp), TODO – anything else?  Reading from
* RAM without function call(!). DON’T USE DIRECTLY FOR COMPARISONS; INSTEAD – USE AS A PART OF DATA OBFUSCATION (IN PARTICULAR, WILL LOOK SIMILAR TO ‘GLOBAL READ OF KNOWN VALUE’ USED TO PREVENT OPTIMIZING OUT). EFFECTIVE PARTIAL COMPARES WHEN USING FOR DATA OBFUSCATION (USING &MASK1 IN ONE PLACE, |MASK2 IN ANOTHER PLACE).  More devious: use the value to generate decryption key, then try to decrypt several pieces of code (with one decrypted by “correct” key, and another by “being-debugged” key, other combinations of “being-debugged” flags also can be accounted for). Then use this code to communicate to the server – which now can distinguish clients which are being debugged (gotcha!). Hare wondering if you are crazy:“Even more devious: use the value to generate encryption key, which is used to encrypt a well-defined constant, which is sent to the server – which then can try different keys to decrypt (gotcha!) \*\* Even more devious: use the value to generate encryption key, which is used to encrypt a well-defined constant, which is sent to the server – which then can try different keys to decrypt (gotcha!)
* “self-debug” (actually – debug a copy of the process). Only one ring 3
* debugger allowed at least in Windows.
* Hiding thread from debugger: NtSetInformationThread, NtCreateThreadEx (reportedly used by Steam at least at some point)
* MOV SS
* INT 2D
* “check within TLS callback” trick
* NB: using Zw\* counterparts \[TODO – elaborate\]
* Messing with debuggers: BLOCKINPUT; NOT REALLY DETECTION, BUT… REP * \[Kulchytskyy\] Most interesting techniques (beyond \[Ferrie\]) NTCREATETHREADEX TO HIDE THREADS Asm to set SEH handlers (32-bit only); on table-based SEH in x64 Windows – see \[NTInsider\] \*\* KiUserExceptionDispatcher
* \[Falliere\].Techniques going beyond previous refs: PUSH SS/POP SS (ACTUALLY, IT IS DESCRIBED IN \[FERRIE\], BUT IMO EXPLANATION HERE IS BETTER) ICE breakpoint (0xF1); not to be confused with SoftICE.  \*\* Scanning for INT 3 (0xCC). False positives. Also should scan for 0xFA \[Falliere\] and probably others. Checksums are generally preferred.
* \[OpenRCE\] Techniques going beyond previous refs: LOCK CMPXCHG8B AS AN INVALID INSTRUCTION TO RAISE SEH Lots of debugger-specific trickery
* \[Tully\]. Techniques going beyond previous refs: REMOVING PE HEADER Messing with debuggers: \*\*\* OutputDebugString Exploit for OllyDbg (TODO: is it still up-to-date?)
* SoftICE detection (doesn’t make much sense now, esp. if your program is 64-bit, but some ideas might be applicable to other debuggers): lots of discussion in \[Crackproof your software\]

