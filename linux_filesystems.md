# Linux - Filesystems, LVM, and you!

Bell Labs was allocated 1% of gross earnings to play and build stuff. UNIX,
the C programming language were created there. Large amounts of free time to
build cool things like this.

Unix is unique because everything in the OS is a file. You can access devices
as if they are files, you can pull data in and out from them, and use all the
standard I/O pipes and redirects.

inodes - collection of metadata about a file. They tell the system what the
file is. Directories, block files, etc are all just special types of files, and
that stuff is defined by the inodes. There is an inode associated with every
file present on the system.

There are no "drives" in linux. Everything mounted on your system is located
somewhere under the / root directory.

#### The original unix filesystem
It was called the "unix filesystem": imagine that. It was slow, and the 'fast
filesystem' (ffs) was developed in response to that.

- 4kb block sizes are default. It can be changed, but it's often not done.
- inodes can be located anywhere on the disk, which makes file seeks faster, and
symlinks
- cylinder groups instead of one large group. Each cylinder group gets its own
superblock

It keeps redundant meta data called superblocks. Helps if you accidentally dd
to the beginning of the filesystem.

#### 1991, Linus teaches himself protected assembly(?)
Linus uses Minix. The shortcoming of this was that it was
never really intended for production use, but rather for study and university
use.

Linus took his own minix system and writes his own kernel for it.

EXT filesystem didn't have enough metadata associated with it. As people started
realizing that you could use this for actual everyday tasks, they started
writing extra features for it. This was when filesystem abstractions started
making an appearance.

VFS is kind of like a special filesystem "API" that would handle the actual
reading/writing data, and all the operating system has to do is call the
virtual filesystem procedures.

#### Ext2
A big step up and is still commonly used as a default boot sector filesystem.

The one real big problem with ext2 is that if the computer is unexpectedly
powered off, the filesystem's integrity is compromised. Basically, it wasn't
really acceptable at scale (terabyte or more).

On any block device (disk), you have datablocks (4kb blocks) that store data.

4kb block sizes are fine for large files, but for small files that have a
remainder less than 4kb, you are essentially wasting space.

#### Ext3
- Added journaling to ext2, which meant you're not stuck in a long fsck anymore,
but you can still lose data.
- backwards compatible

#### Ext4
- somewhat backwards compatible (can't mount ext4 as earlier, but can mount ext2/3 as ext4)
- no limit on the amount of subdirectories b+tree

#### SGI (XFS)
- used by nintendo
- standardized 64-bit filesystems (created XFS)
- designed to be hot resized. It can be resized while in use.
- scales really well at multi-TB levels
- set up to allow multiple processes to use the disk at once
- btrees take away some limits of filesystems (unlimited subdirectories)

#### LVM - Logical Volume Management
- Allows you to grow
- Allows you to aggregate multiple hard drives and create one very large partition

#### Others
- eMC
- netApp
- ZXFS (SUN)
- JFS (IBM)
- ReiserFS (allows for tail packing)
