/*
 * PCIe 寄存器读写工具 - 模拟芯潮流高速接口芯片寄存器操作
 * 用于驱动/固件测试中的寄存器配置验证
 * 编译: gcc -o pcie_reg_rw pcie_reg_rw.c -O2
 */

#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/mman.h>
#include <stdint.h>

#define PAGE_SIZE 4096

void print_usage() {
    printf("Usage:\n");
    printf("  ./pcie_reg_rw read <bar_address> <offset> [size]\n");
    printf("  ./pcie_reg_rw write <bar_address> <offset> <value>\n");
    printf("Example: ./pcie_reg_rw read 0xf0000000 0x100\n");
}

int main(int argc, char *argv[]) {
    if (argc < 4) {
        print_usage();
        return 1;
    }

    char *mode = argv[1];
    unsigned long bar_addr = strtoul(argv[2], NULL, 0);
    unsigned long offset = strtoul(argv[3], NULL, 0);

    if (strcmp(mode, "read") == 0) {
        int size = (argc > 4) ? atoi(argv[4]) : 4;
        printf("Reading BAR 0x%lx + offset 0x%lx (size %d bytes)\n", bar_addr, offset, size);
        // 实际项目中会用 /dev/mem + mmap，这里模拟输出
        printf("[SIM] Register value at 0x%lx: 0x%08X (PCIe Config Space)\n", bar_addr + offset, 0x12345678);
        printf("常见寄存器：Command=0x%04X, Status=0x%04X\n", 0x0007, 0x0010);
    } 
    else if (strcmp(mode, "write") == 0) {
        uint32_t value = strtoul(argv[4], NULL, 0);
        printf("Writing 0x%08X to BAR 0x%lx + 0x%lx\n", value, bar_addr, offset);
        printf("[SIM] Write successful (模拟驱动寄存器配置)\n");
    } 
    else {
        print_usage();
        return 1;
    }
    return 0;
}
