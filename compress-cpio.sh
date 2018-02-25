tree serverTree/ -fi | head -n $(( `tree -fi serverTree | wc -l` - 2)) | cpio -o > serverTree.cpio
